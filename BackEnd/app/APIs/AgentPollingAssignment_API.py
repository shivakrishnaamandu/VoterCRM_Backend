from app.__init__ import db, application
from app.APIs import Agents_API
from app.Models.Agents import *
from app.Models.Logins import *
from app.Models.AdminCandidateMapping import *
from app.Models.Subscriptions import *
from app.Models.Candidates import *
from app.Models.PollingStations import *
from app.Models.AgentPollingAssignment import *
from app.Models.AssemblyConstituency import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from app.Authentication.hashingservice import HashingService
from flask import request, Blueprint, Response
from sqlalchemy import inspect, and_
from werkzeug import exceptions
import csv, io
import requests
import re, random, string, secrets


sign_up_key = "signupkey"
jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)
hashing_service = HashingService()

application.before_request(lambda: middleware.auth(request))

AgentPollingAssignemnt_API_blueprint = Blueprint("AgentPollingAssignment_API", __name__)

@AgentPollingAssignemnt_API_blueprint.route("/admin/upload_agentpollingassignment", methods=["POST"])
def upload():

    # authentication
    print(f'request.headers.get("sign_up_key"): {request.headers.get("signupkey")}')
    print(f"sign_up_key: {sign_up_key}")
    if request.headers.get("signupkey") != sign_up_key:
        return exceptions.Unauthorized(description="Incorrect Key")

    file = request.files['file']

    # getting headers for authentication in redirected APIs
    req_token = request.headers["token"]
    req_signupkey = request.headers["signupkey"]
    req_headers = {'signupkey': req_signupkey, 'token': req_token}

    # storing the created username, password for the corresponding Agent Id in excel
    username_pwd_dict = dict()

    # reading csv file
    if file:

        csv_data = csv.reader(io.StringIO(file.read().decode("utf-8")))
        next(csv_data)
        
        for row in csv_data:

            (Agent_Id, First_name, Last_name, Email_Id, 
             Gender, Phone_No, Address, polling_station_no) = (row[0], row[1], row[2], 
                                                               row[3], row[4], row[5],
                                                               row[6], row[7])

            # calling function to redirect
            resp_username, resp_pwd, response = redirect_agent_signup(First_name, Last_name, Email_Id, Gender, Phone_No, Address, req_headers) 
            username_pwd_dict[Agent_Id] = [resp_pwd, resp_username]

            # Return the status code 
            if not response.ok:
                return f"""File not uploaded. \nError with Status Code: {response.status_code}. 
                            \nUploaded Agents with their username and password {username_pwd_dict}"""
            
            db.session.commit()

            add_data_to_AgentPollingAssignment(req_token, resp_username, polling_station_no)

        return f'File uploaded and data loaded, Agent SignIn  credentials are: \n {username_pwd_dict}'


# function to redirect to agent signup API
def redirect_agent_signup(First_name, Last_name, Email_Id, Gender, Phone_No, Address, req_headers):

    # generating username by concatenating First_Name and Last_Name
    # limiting First_name in Username to 10 letters
    Username = re.sub("[^A-Za-z]+", "", First_name)
    if len(Username) > 10:
        Username = Username[:10]
    
    Username = Username + Last_name[:1]
    temp_username = Username
    
    # if the Username already exists append it with numbers till 99
    agent = Agents.query.filter_by(Username = Username).first()
    while agent and agent.Username == temp_username:
        temp_username = Username + str(random.randint(1, 99))
        agent = Agents.query.filter_by(Username = temp_username).first()
    
    Username = temp_username
    
    # Randomly create password for User with Uppercase letters and digits
    Password = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(8))

    agent_data = {'First_name': First_name, 
                  'Last_name': Last_name, 
                  'Username': Username, 
                  'Password': Password, 
                  'Email_Id': Email_Id,
                  'IsAdmin': 0,
                  'Gender': Gender,
                  'Phone_No': Phone_No,
                  'Address': Address
                  }

    response = requests.post(url= request.host_url.rstrip("/") + "/agent/signup", json= agent_data, headers= req_headers)
    return Username, Password, response

def add_data_to_AgentPollingAssignment(req_token, resp_username, polling_station_no):
    
    # get the agent id based on the token 
    login = Logins.query.filter_by(Token = req_token).first()
    admin_id = login.User_Id

    # get the candidate id based on agent_id
    mapping = AdminCandidateMapping.query.filter_by(Admin_Id = admin_id).first()
    candidate_id = mapping.Candidate_Id

    # get subscription id based on candidate id
    subscription = Subscription.query.filter_by(Candidate_Id = candidate_id).first()
    subscription_id = subscription.Subscription_Id

    # get Agent_Id based on username
    agent = Agents.query.filter_by(Username = resp_username).first()
    agent_id = agent.Agent_Id

    # get constituency name
    candidate = Candidates.query.filter_by(Candidate_Id = candidate_id).first()
    constituency_id = candidate.Candidate_Constituency

    constituency = AssemblyConstituency.query.filter_by(Constituency_Id = constituency_id).first()
    constituency_name = constituency.Constituency_Name

    # get polling station id 
    polling_station = PollingStations.query.filter_by(Assembly_Constituency_Name = constituency_name, Polling_Station_No = polling_station_no).first()
    polling_station_id = polling_station.Polling_Station_Id

    assignment = AgentPollingAssignment(Agent_Id=agent_id, 
                                        Polling_Station_Code=polling_station_id,
                                        Candidate_Id=candidate_id,
                                        Subscription_Id=subscription_id,
                                        Assignment_Status='Assigned')
    
    db.session.add(assignment)
    db.session.commit()
    return f'Mapping added successfully for {resp_username}'


"""
Doubts_1: 
1. would we create the username. if yes then how to assign the username. what about when we have the same username
            yes, we will be creating the username. if already present then append number
2. where would you store the data related to admin (candidate assigned to, political party etc).
            db team creating table for that
3. can a candidate have multiple subscriptions
            consider 1-1
4. is the candidate name unique
            check with team
5. shouldnt signup api be a post method since we are adding a new record

Doubts_2:
1. How to map the get the polling station code
2. What are the assignment statuses

CSV format:
1. Agent_id: it is for admin reference (will not be entered in our DB)
2. First_Name of agent
3. Last_name of agent
4. Email_id of agent
5. Phone number of agent
6. Address of agent
7. Polling station number of Constituency in our DB (nummber to be given to the agent)

Steps:
1. upload data using post method (csv format mentioned above)
2. redirecting to agent/signup api for agent signup
3. create an agent -> signup
            generate username and password
            Add to Agents table
4. commit DB
5. call assignment function with arguments: headers, username, polling_station_no
6. get agent id, polling_station_id, candidate_id and subscription_id with queries
7. add to AgentPollingAssignment table
8. commit
9. return/display Agent_id, username and password

columns needed in the csv:
    Agents table:
        first name
        last name
        email_id
        gender 
        phone number
        address
    Candidates table:
        Candidate Name (to get candidate ID)
    PollingStation table:
        (to get polling station code)
        Polling Station Name
        Polling Station location
    Subscriptions
        Subscription ID (query with the candidate id)

"""

"""
Username Creation:
    - first name start full(max length 10) 
    - lastname first letter
    - 2 random numbers suffix if username is not unique

Password Creation:
    - Maxlength = 8
    - Random combination of letters and digits
"""

