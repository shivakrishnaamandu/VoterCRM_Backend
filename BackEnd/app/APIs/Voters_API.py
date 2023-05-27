from app.__init__ import application, db
from app.Models.Voters import *
from app.Models.PollingStations import *
from app.Models.Relations import *

from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint
import csv, io
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

Voters_API_blueprint = Blueprint("Voters_API", __name__)


@Voters_API_blueprint.route('/admin/upload_voters', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # Read the uploaded CSV file
        csv_data = csv.reader(io.StringIO(file.read().decode('utf-8')))
        next(csv_data)  # Skip header row if needed
        for row in csv_data:
            # Assuming the CSV columns are in the order of column1, column2
            data = Voters(uuid.uuid1().int>>97,row[2],row[3],row[4],row[5],row[8],row[6],row[7],row[11])
            db.session.add(data)
            db.session.commit()
        return 'File uploaded and data inserted into the database table successfully.'


@Voters_API_blueprint.route("/admin/list_voters")
def get_all_voters():
    print(f"url accessed")
    voters = Voters.query.all()
    if voters:
        voter_list = []
        for voter in voters:
            print(f"Voter Name: {voter.Voters_Name}")
            voter_dict = {}
            voter_dict["VoterId"] = voter.Voters_Id
            voter_dict["VoterName"] = voter.Voters_Name
            voter_dict["VoterNo"] = voter.Voters_No
            voter_list.append(voter_dict)
        return {"voters": voter_list}
    else:
        return {"message": "No voters Available"}
