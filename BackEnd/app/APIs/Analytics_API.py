from app.__init__ import application, db
from app.Models.VoterDetails import *
from app.Models.PollingStations import *
from app.Models.AssemblyConstituency import *
from app.Models.Districts import *
from app.Models.States import *
from app.Models.Logins import *
from app.Models.AgentPollingAssignment import *
from sqlalchemy import inspect, and_
from io import StringIO
from werkzeug import exceptions
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, Response, jsonify
import csv, io
import uuid

jwt_secret = "secret"
sign_up_key = "signupkey"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

Analytics_API_blueprint = Blueprint("Analytics_API", __name__)


@Analytics_API_blueprint.route("/admin/get_voter_details", methods=["POST"])
def upload():
    body = request.json
    state_names = body["state_names"]
    district_names = body["district_names"]
    constituency_names = body["constituency_names"]
    polling_booth_names = body["polling_booth_names"]

    query = db.session.query(VoterDetails)

    # Apply filters based on hierarchy order
    if len(polling_booth_names) > 0:
        query = query.join(
            PollingStations,
            and_(
                PollingStations.Polling_Station_No == VoterDetails.polling_booth_no,
                PollingStations.Assembly_Constituency_Name
                == VoterDetails.constituency_name,
            ),
        ).filter(PollingStations.Polling_Station_Name.in_(polling_booth_names))
    else:
        query = query.join(
            PollingStations,
            and_(
                PollingStations.Polling_Station_No == VoterDetails.polling_booth_no,
                PollingStations.Assembly_Constituency_Name
                == VoterDetails.constituency_name,
            ),
        )

    if len(constituency_names) > 0:
        query = query.join(
            AssemblyConstituency,
            AssemblyConstituency.Constituency_Name
            == PollingStations.Assembly_Constituency_Name,
        ).filter(AssemblyConstituency.Constituency_Name.in_(constituency_names))
    else:
        query = query.join(
            AssemblyConstituency,
            AssemblyConstituency.Constituency_Name
            == PollingStations.Assembly_Constituency_Name,
        )

    if len(district_names) > 0:
        query = query.join(
            Districts, Districts.District_Id == AssemblyConstituency.District_Code
        ).filter(Districts.District_Name.in_(district_names))
    else:
        query = query.join(
            Districts, Districts.District_Id == AssemblyConstituency.District_Code
        )

    if len(state_names) > 0:
        query = query.join(States, States.State_Id == Districts.State_Code).filter(
            States.State_Name.in_(state_names)
        )
    else:
        query = query.join(States, States.State_Id == Districts.State_Code)

    voterdetails = query.all()
    # print(voterdetails)

    # Convert voters to JSON response
    voterdetails_data = []
    for voterdetail in voterdetails:
        voterdetail_data = voterdetail.__dict__.copy()
    # Remove internal attributes
        voterdetail_data.pop("_sa_instance_state", None)
        voterdetails_data.append(voterdetail_data)

    return {"votersdetails": voterdetails_data}


@Analytics_API_blueprint.route("/agent/get_voter_details", methods=["GET"])
def get_agent_voter_details():

    # authentication
    print(
        f'request.headers.get("sign_up_key"): {request.headers.get("signupkey")}')
    print(f"sign_up_key: {sign_up_key}")
    if request.headers.get("signupkey") != sign_up_key:
        return exceptions.Unauthorized(description="Incorrect Key")
    
    # getting token header to find the agent
    req_token = request.headers["token"]

    login = Logins.query.filter_by(Token=req_token).first()
    agent_id = login.User_Id

    # '1': ['7D5LUR63', 'NameL'], '2': ['EPBHZ1F1', 'NameL75']}

    assignment = AgentPollingAssignment.query.filter_by(Agent_Id = agent_id).first()
    polling_station_id = assignment.Polling_Station_Code

    polling_station = PollingStations.query.filter_by(Polling_Station_Id = polling_station_id).first()

    voterdetails = VoterDetails.query.filter_by(constituency_name = polling_station.Assembly_Constituency_Name,
                                                polling_booth_no = polling_station.Polling_Station_No).all()
    
    # Convert voters to JSON response
    voterdetails_data = []
    for voterdetail in voterdetails:
        voterdetail_data = voterdetail.__dict__.copy()
    # Remove internal attributes
        voterdetail_data.pop("_sa_instance_state", None)
        voterdetails_data.append(voterdetail_data)

    return {"votersdetails": voterdetails_data}


"""
get agent_id from logins table
get polling station assignment of the agent
get voterdetail from that particular station
"""
