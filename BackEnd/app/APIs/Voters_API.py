from app.__init__ import application, db
from app.Models.Voters import *
from app.Models.PollingStations import *
from app.Models.Relations import *
from app.Models.AssemblyConstituency import *
from app.Models.Districts import *
from app.Models.States import *
from sqlalchemy import inspect, and_
from io import StringIO

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
            if row[1] is None or row[1] == "":
                while True:
                    # Generate a unique 10-digit UUID with integer characters
                    generated_uuid = str(uuid.uuid4().int)[:10]
                    # Check if the generated UUID is already present in the table
                    if not Voters.query.filter_by(Voter_UID=generated_uuid).first():
                        break
                row[1] = generated_uuid

            # Assuming the CSV columns are in the order of column1, column2
            (
                Voter_UID,
                Voter_Name,
                Relative_Name,
                Relation_Type,
                House_Number,
                Age,
                Gender,
                Assembly_Constituency_Name,
                Polling_Station_No,
            ) = (
                row[1],
                row[2],
                row[3],
                row[4],
                row[7],
                row[5],
                row[6],
                row[11],
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
                Assembly_Constituency_Name,
                Polling_Station_No,
            )
            db.session.add(data)
            db.session.commit()
        return {
            "message": "File uploaded and data inserted into the database table successfully."
        }


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
            and_(
                PollingStations.Polling_Station_No == Voters.Polling_Station_No,
                PollingStations.Assembly_Constituency_Name
                == Voters.Assembly_Constituency_Name,
            ),
        )
        .join(
            AssemblyConstituency,
            AssemblyConstituency.Constituency_Name
            == PollingStations.Assembly_Constituency_Name,
        )
        .join(Districts, Districts.District_Id == AssemblyConstituency.District_Code)
        .join(States, States.State_Id == Districts.State_Code)
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
            print(f"Voter Name: {voter.Voter_Name}")
            voter_dict = {}
            voter_dict["Voter_Row_ID"] = voter.Voter_Row_ID
            voter_dict["Voter_UID"] = voter.Voter_UID
            voter_dict["VoterName"] = voter.Voter_Name
            voter_dict["Relative_Name"] = voter.Relative_Name
            voter_dict["Relation_Type"] = voter.Relation_Type
            voter_dict["House_Number"] = voter.House_Number
            voter_dict["Age"] = voter.Age
            voter_dict["Gender"] = voter.Gender
            voter_dict["Assembly_Constituency_Name"] = voter.Assembly_Constituency_Name
            voter_dict["Polling_Station_No"] = voter.Polling_Station_No
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
            and_(
                PollingStations.Polling_Station_No == Voters.Polling_Station_No,
                PollingStations.Assembly_Constituency_Name
                == Voters.Assembly_Constituency_Name,
            ),
        )
        .join(
            AssemblyConstituency,
            AssemblyConstituency.Constituency_Name
            == PollingStations.Assembly_Constituency_Name,
        )
        .join(Districts, Districts.District_Id == AssemblyConstituency.District_Code)
        .join(States, States.State_Id == Districts.State_Code)
        .filter(
            States.State_Name == State_Name,
            Districts.District_Name == District_Name,
            AssemblyConstituency.Constituency_Name == Constituency_Name,
        )
        .all()
    )
    if voters:
        # Create a StringIO object to write the CSV data
        csv_data = StringIO()

        # Create a CSV writer
        csv_writer = csv.writer(csv_data)

        # Write the header row
        csv_writer.writerow(inspect(Voters).columns.keys())

        # Write the polling station data
        for voter in voters:
            # Extract the desired attributes from the voter object
            row = [
                voter.Voter_Row_ID,
                voter.Voter_UID,
                voter.Voter_Name,
                voter.Relative_Name,
                voter.Relation_Type,
                voter.House_Number,
                voter.Age,
                voter.Gender,
                voter.Assembly_Constituency_Name,
                voter.Polling_Station_No,
            ]
            csv_writer.writerow(row)

        # Create a response with the CSV file
        response = Response(csv_data.getvalue(), mimetype="text/csv")
        response.headers.set(
            "Content-Disposition", "attachment", filename="voterlist.csv"
        )

        return response
    else:
        return {"message": "No pollingstation data available"}
