from app.__init__ import application, db
from app.Models.PollingStations import *
from app.Models.AssemblyConstituency import *
from app.Models.Districts import *
from app.Models.States import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, Response
from sqlalchemy import inspect
import csv, io
from io import StringIO
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

PollingStation_API_blueprint = Blueprint("PollingStation_API", __name__)


# we are uploading polling station data in csv right? or Are we physcally adding?
@PollingStation_API_blueprint.route("/admin/upload_pollingstations", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        # Read the uploaded CSV file
        csv_data = csv.reader(io.StringIO(file.read().decode("utf-8")))
        next(csv_data)  # Skip header row if needed
        for row in csv_data:
            (
                Polling_Station_Name,
                Polling_Station_No,
                Polling_Station_Location,
                Assembly_Constituency_Code,
            ) = (
                row[1],
                row[0],
                row[2],
                row[4],
            )
            data = PollingStations(
                Polling_Station_Name,
                Polling_Station_No,
                Polling_Station_Location,
                Assembly_Constituency_Code,
            )
            db.session.add(data)
            db.session.commit()
        return {"message": "File uploaded and data inserted into the database table successfully."}


@PollingStation_API_blueprint.route("/admin/list_pollingstations", methods=["POST"])
def get_all_pollingstations():
    print(f"url accessed")
    body = request.json
    State_Name = body["State_Name"]
    District_Name = body["District_Name"]
    Constituency_Name = body["Constituency_Name"]

    pollingstations = (
        db.session.query(PollingStations)
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
            PollingStations.Assembly_Constituency_Name == Constituency_Name,
        )
        .all()
    )
    if pollingstations:
        pollingstations_list = []
        for pollingstation in pollingstations:
            print(f"Polling Station Name: {pollingstation.Polling_Station_Name}")
            polling_station_dict = {}
            polling_station_dict["Polling_Station_Id"] = pollingstation.Polling_Station_Id
            polling_station_dict["Polling_Station_Name"] = pollingstation.Polling_Station_Name
            polling_station_dict["Polling_Station_No"] = pollingstation.Polling_Station_No
            polling_station_dict["Polling_Station_Location"] = pollingstation.Polling_Station_Location
            polling_station_dict["Assembly_Constituency_Name"] = pollingstation.Assembly_Constituency_Name

            pollingstations_list.append(polling_station_dict)

        return {"polling_stations": pollingstations_list}
    else:
        return {"message": "No polling stations available"}


@PollingStation_API_blueprint.route("/admin/download_pollingstations", methods=["POST"])
def download_all_pollingstations():
    print(f"url accessed")
    body = request.json
    State_Name = body["State_Name"]
    District_Name = body["District_Name"]
    Constituency_Name = body["Constituency_Name"]

    pollingstations = (
        db.session.query(PollingStations)
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
            PollingStations.Assembly_Constituency_Name == Constituency_Name,
        )
        .all()
    )
    if pollingstations:
        # Create a StringIO object to write the CSV data
        csv_data = StringIO()

        # Create a CSV writer
        csv_writer = csv.writer(csv_data)

        # Write the header row
        csv_writer.writerow(inspect(PollingStations).columns.keys())

        # Write the polling station data
        for pollingstation in pollingstations:
            # Extract the desired attributes from the pollingstation object
            row = [
                pollingstation.Polling_Station_Id,
                pollingstation.Polling_Station_Name,
                pollingstation.Polling_Station_No,
                pollingstation.Polling_Station_Location,
                pollingstation.Assembly_Constituency_Name,
            ]
            csv_writer.writerow(row)

        # Create a response with the CSV file
        response = Response(csv_data.getvalue(), mimetype="text/csv")
        response.headers.set(
            "Content-Disposition", "attachment", filename="pollingstations.csv"
        )

        return response
    else:
        return {"message": "No pollingstation data available"}


# @PollingStation_API_blueprint.route("/admin/list_polling_station", methods=["POST"])
# def PollingStation_list():
#     assemby_constituency_code = request.json["Assemby_Constituency_Code"]  # Fetch PollingStation by assembly constituency code
#     try:
#         PollingStation_by_const = PollingStations.query.filter_by(Assemby_Constituency_Code=assemby_constituency_code).all()
#         if PollingStation_by_const:
#             polling_station_list = []
#             for polling_station in PollingStation_by_const:
#                 polling_station_dict = {}
#                 polling_station_dict["Polling_Station_Id"] = polling_station.Polling_Station_Id
#                 polling_station_dict["Polling_Station_Name"] = polling_station.Polling_Station_Name
#                 polling_station_dict["Polling_Station_No"] = polling_station.Polling_Station_No
#                 polling_station_dict["Polling_Station_Location"] = polling_station.Polling_Station_Location
#                 polling_station_dict["Assemby_Constituency_Code"] = polling_station.Assemby_Constituency_Code
#                 polling_station_list.append(polling_station_dict)
#             return {"PollingStation": polling_station_list}
#         else:
#             return {"message": "No Polling Station available in the constituency"}
#     except:
#         return {"message": "Error fetching Polling Station"}


# @PollingStation_API_blueprint.route("/admin/add_polling_station", methods=["POST"])
# def add_polling_station():
#     body = request.json
#     polling_station = PollingStations(
#         uuid.uuid1().int >> 97,
#         body["Polling_Station_Name"],
#         body["Polling_Station_No"],
#         body["Polling_Station_Location"],
#         body["Assemby_Constituency_Code"],
#     )
#     db.session.add(polling_station)
#     db.session.commit()
#     return {"message": "New Polling Station added successfully"}


# @PollingStation_API_blueprint.route("/admin/delete_polling_station", methods=["POST"])
# def delete_polling_station():
#     polling_station_id = request.json["Polling_Station_Id"]
#     print(polling_station_id)
#     try:
#         PollingStations.query.filter_by(
#             Polling_Station_Id=polling_station_id
#         ).delete()  # Fetching the instance
#         db.session.commit()
#         return {"message": "Polling Station deleted successfully"}
#     except:
#         return {"message": "Error deleting Polling Station"}


# @PollingStation_API_blueprint.route("/admin/update_polling_station", methods=["POST"])
# # Can update 3 fields Polling_Station_Name , Polling_Station_No, Polling_Station_Location
# def update_polling_station():
#     try:
#         polling_station_id, Updated_ps_name, Updated_ps_no, Updated_ps_loc = (
#             request.json["Polling_Station_Id"],
#             request.json["To_Update_Dist_Name"],
#             request.json["To_Update_Dist_No"],
#             request.json["To_Update_Dist_Location"],
#         )
#         existing_polling_station = PollingStations.query.filter_by(Polling_Station_Id=polling_station_id).first()
#         if existing_polling_station:
#             existing_polling_station.Polling_Station_Name = Updated_ps_name
#             existing_polling_station.Polling_Station_No = Updated_ps_no
#             existing_polling_station.Polling_Station_Location = Updated_ps_loc
#             print(existing_polling_station.Polling_Station_Name)
#             db.session.commit()
#             db.session.close()
#             return {"message": "Polling Station updated successfully"}
#         else:
#             return {"message": "Polling Station not available"}
#     except Exception as e:
#         db.session.rollback()
#         return {"Error: " + str(e)}
#     finally:
#         db.session.close()
