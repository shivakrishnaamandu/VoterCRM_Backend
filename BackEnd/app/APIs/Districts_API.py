from app.__init__ import application, db
from app.Models.Districts import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, jsonify
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

Districts_API_blueprint = Blueprint("Districts_API", __name__)


@Districts_API_blueprint.route("/admin/districts_list", methods=["POST"])
def districts_list():
    state_code = request.json["State_Code"]  # Fetch districts by state code
    try:
        districts_by_state = Districts.query.filter_by(State_Code=state_code).all()
        if districts_by_state:
            district_list = []
            for district in districts_by_state:
                district_dict = {}
                district_dict["District_Id"] = district.District_Id
                district_dict["District_Name"] = district.District_Name
                district_dict["District_No"] = district.District_No
                district_dict["State_Code"] = district.State_Code
                district_list.append(district_dict)
            return {"districts": district_list}
        else:
            return {"message": "No districts available in the state"}
    except:
        return {"message": "Error deleting districts"}


@Districts_API_blueprint.route("/admin/add_district", methods=["POST"])
def add_district():
    body = request.json
    district = Districts(
        body["District_Name"],
        body["District_No"],
        body["State_Code"],
    )
    db.session.add(district)
    db.session.commit()
    return {"message": "New district added successfully"}


@Districts_API_blueprint.route("/admin/delete_district", methods=["POST"])
def delete_district():
    district_id = request.json["District_Id"]
    print(district_id)
    try:
        Districts.query.filter_by(
            District_Id=district_id
        ).delete()  # Fetching the instance
        db.session.commit()
        return {"message": "District deleted successfully"}
    except:
        return {"message": "Error deleting districts"}


@Districts_API_blueprint.route("/admin/update_district", methods=["POST"])
# Can update 2 fields District_Name , District_No
def update_district():
    try:
        district_id, Updated_dist_name, Updated_dist_no = (
            request.json["District_Id"],
            request.json["To_Update_Dist_Name"],
            request.json["To_Update_Dist_No"],
        )
        existing_district = Districts.query.filter_by(District_Id=district_id).first()
        if existing_district:
            existing_district.District_Name = Updated_dist_name
            existing_district.District_No = Updated_dist_no
            print(existing_district.District_Name)
            db.session.commit()
            db.session.close()
            return {"message": "District updated successfully"}
        else:
            return {"message": "District Not available"}
    except Exception as e:
        db.session.rollback()
        return jsonify("Error: " + str(e))
    finally:
        db.session.close()
