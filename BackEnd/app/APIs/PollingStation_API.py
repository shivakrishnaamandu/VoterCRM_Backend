from app.__init__ import application, db
from app.Models.PollingStations import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

PollingStation_API_blueprint = Blueprint("PollingStation_API", __name__)


@PollingStation_API_blueprint.route("/admin/list_polling_station", methods=["POST"])
def PollingStation_list():
    assemby_constituency_code = request.json["Assemby_Constituency_Code"]  # Fetch PollingStation by assembly constituency code
    try:
        PollingStation_by_const = PollingStations.query.filter_by(Assemby_Constituency_Code=assemby_constituency_code).all()
        if PollingStation_by_const:
            polling_station_list = []
            for polling_station in PollingStation_by_const:
                polling_station_dict = {}
                polling_station_dict["Polling_Station_Id"] = polling_station.Polling_Station_Id
                polling_station_dict["Polling_Station_Name"] = polling_station.Polling_Station_Name
                polling_station_dict["Polling_Station_No"] = polling_station.Polling_Station_No
                polling_station_dict["Polling_Station_Location"] = polling_station.Polling_Station_Location
                polling_station_dict["Assemby_Constituency_Code"] = polling_station.Assemby_Constituency_Code
                polling_station_list.append(polling_station_dict)
            return {"PollingStation": polling_station_list}
        else:
            return {"message": "No Polling Station available in the constituency"}
    except:
        return {"message": "Error fetching Polling Station"}


@PollingStation_API_blueprint.route("/admin/add_polling_station", methods=["POST"])
def add_polling_station():
    body = request.json
    polling_station = PollingStations(
        uuid.uuid1().int >> 97,
        body["Polling_Station_Name"],
        body["Polling_Station_No"],
        body["Polling_Station_Location"],
        body["Assemby_Constituency_Code"],
    )
    db.session.add(polling_station)
    db.session.commit()
    return {"message": "New Polling Station added successfully"}


@PollingStation_API_blueprint.route("/admin/delete_polling_station", methods=["POST"])
def delete_polling_station():
    polling_station_id = request.json["Polling_Station_Id"]
    print(polling_station_id)
    try:
        PollingStations.query.filter_by(
            Polling_Station_Id=polling_station_id
        ).delete()  # Fetching the instance
        db.session.commit()
        return {"message": "Polling Station deleted successfully"}
    except:
        return {"message": "Error deleting Polling Station"}


@PollingStation_API_blueprint.route("/admin/update_polling_station", methods=["POST"])
# Can update 3 fields Polling_Station_Name , Polling_Station_No, Polling_Station_Location
def update_polling_station():
    try:
        polling_station_id, Updated_ps_name, Updated_ps_no, Updated_ps_loc = (
            request.json["Polling_Station_Id"],
            request.json["To_Update_Dist_Name"],
            request.json["To_Update_Dist_No"],
            request.json["To_Update_Dist_Location"],
        )
        existing_polling_station = PollingStations.query.filter_by(Polling_Station_Id=polling_station_id).first()
        if existing_polling_station:
            existing_polling_station.Polling_Station_Name = Updated_ps_name
            existing_polling_station.Polling_Station_No = Updated_ps_no
            existing_polling_station.Polling_Station_Location = Updated_ps_loc
            print(existing_polling_station.Polling_Station_Name)
            db.session.commit()
            db.session.close()
            return {"message": "Polling Station updated successfully"}
        else:
            return {"message": "Polling Station not available"}
    except Exception as e:
        db.session.rollback()
        return {"Error: " + str(e)}
    finally:
        db.session.close()
