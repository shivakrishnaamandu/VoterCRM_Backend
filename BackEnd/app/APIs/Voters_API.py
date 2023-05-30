from app.__init__ import application, db
from app.Models.Voters import *
from app.Models.PollingStations import *
from app.Models.Relations import *
from app.Models.AssemblyConstituency import *
from app.Models.Districts import *
from app.Models.States import *
from sqlalchemy import inspect

from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, Response
import csv, io
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

Voters_API_blueprint = Blueprint("Voters_API", __name__)


@Voters_API_blueprint.route("/admin/upload_voters", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        # Read the uploaded CSV file
        csv_data = csv.reader(io.StringIO(file.read().decode("utf-8")))
        next(csv_data)  # Skip header row if needed
        for row in csv_data:
            # Check if the UUID column is null in the data
            if row[2] is None or row[2] == "":
                while True:
                    # Generate a unique 10-digit UUID with integer characters
                    generated_uuid = str(uuid.uuid4().int)[:10]
                    # Check if the generated UUID is already present in the table
                    if not Voters.query.filter_by(Voter_UID=generated_uuid).first():
                        break
                row[2] = generated_uuid

            # Assuming the CSV columns are in the order of column1, column2
            (
                Voter_UID,
                Voter_Name,
                Relative_Name,
                Relation_Type,
                House_Number,
                Age,
                Gender,
                Polling_Station_Code,
            ) = (
                row[1],
                row[2],
                row[3],
                row[4],
                row[7],
                row[5],
                row[6],
                row[10],
            )
            data = Voters(
                Voter_UID,
                Voter_Name,
                Relative_Name,
                Relation_Type,
                House_Number,
                Age,
                Gender,
                Polling_Station_Code,
            )
            db.session.add(data)
            db.session.commit()
        return "File uploaded and data inserted into the database table successfully."


@Voters_API_blueprint.route("/admin/list_voters", methods=["POST"])
def get_all_voters():
    print(f"url accessed")
    body = request.json
    State_Name = body["State_Name"]
    District_Name = (body["District_Name"],)
    Constituency_Name = (body["Constituency_Name"],)

    voters = (
        db.session.query(Voters)
        .join(
            PollingStations,
            PollingStations.Polling_Station_Id == Voters.Polling_Station_Code,
        )
        .join(
            AssemblyConstituency,
            AssemblyConstituency.Constituency_Id
            == PollingStations.Assembly_Constituency_Code,
        )
        .join(Districts, Districts.District_Id == AssemblyConstituency.District_Code)
        .join(States, States.States_Id == Districts.State_Code)
        .filter(
            States.State_Name == State_Name,
            Districts.District_Name == District_Name,
            AssemblyConstituency.Constituency_Name == Constituency_Name,
        )
        .all()
    )
    if voters:
        voter_list = []
        for voter in voters:
            print(f"Voter Name: {voter.Voters_Name}")
            voter_dict = {}
            voter_dict["Voter_Row_ID"] = voter.Voter_Row_ID
            voter_dict["Voter_UID"] = voter.Voter_UID
            voter_dict["VoterName"] = voter.Voters_Name
            voter_dict["Relative_Name"] = voter.Relative_Name
            voter_dict["Relation_Type"] = voter.Relation_Type
            voter_dict["House_Number"] = voter.House_Number
            voter_dict["Age"] = voter.Age
            voter_dict["Gender"] = voter.Gender
            voter_dict["Polling_Station_Code"] = voter.Polling_Station_Code
            voter_list.append(voter_dict)
        return {"voters": voter_list}
    else:
        return {"message": "No voters Available"}


@Voters_API_blueprint.route("/admin/download_voters", methods=["POST"])
def download_all_voters():
    print(f"url accessed")
    body = request.json
    State_Name = body["State_Name"]
    District_Name = (body["District_Name"],)
    Constituency_Name = (body["Constituency_Name"],)

    voters = (
        db.session.query(Voters)
        .join(
            PollingStations,
            PollingStations.Polling_Station_Id == Voters.Polling_Station_Code,
        )
        .join(
            AssemblyConstituency,
            AssemblyConstituency.Constituency_Id
            == PollingStations.Assembly_Constituency_Code,
        )
        .join(Districts, Districts.District_Id == AssemblyConstituency.District_Code)
        .join(States, States.States_Id == Districts.State_Code)
        .filter(
            States.State_Name == State_Name,
            Districts.District_Name == District_Name,
            AssemblyConstituency.Constituency_Name == Constituency_Name,
        )
        .all()
    )
    if voters:
        # Create a CSV string using the voter data
        csv_data = []
        for voter in voters:
            csv_data.append([voter])

        # Create a response with the CSV file
        response = Response(content_type="text/csv")
        response.headers.set("Content-Disposition", "attachment", filename="voters.csv")

        # Write the CSV data to the response
        csv_writer = csv.writer(response)
        csv_writer.writerow(inspect(Voters).columns.keys())  # Write header row
        csv_writer.writerows(csv_data)

        return response
    else:
        return {"message": "No voter data available"}
