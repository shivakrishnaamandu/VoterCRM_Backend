from app.__init__ import application, db
from app.Models.AssemblyConstituency import *
from app.Models.Districts import *
from app.Models.States import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, jsonify
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

AssemblyConstituency_API_blueprint = Blueprint("AssemblyConstituency_API", __name__)


@AssemblyConstituency_API_blueprint.route("/admin/assemblyconstituency", methods=["POST"])
def get_all_constituencies():
    try:
        body= request.json
        if "District_Name" in body:
            district_name = request.json["District_Name"]
            dis = Districts.query.filter_by(District_Name=district_name).one()
            constituency_district = AssemblyConstituency.query.filter_by(District_Code=dis.District_Id).all()

            if constituency_district:
                constituency_list = []
                for constituency in constituency_district:
                    constituency_dict = {}
                    constituency_dict["Constituency_Id"] = constituency.Constituency_Id
                    constituency_dict["Constituency_Name"] = constituency.Constituency_Name
                    constituency_dict["Constituency_No"] = constituency.Constituency_No
                    constituency_dict["District_Code"] = constituency.District_Code
                    constituency_list.append(constituency_dict)
                return {"constituency": constituency_list}
        if "State_Name" in body:
            constituency_list = []
            state_name = request.json["State_Name"]
            print("0")
            print(state_name)
            state = States.query.filter_by(State_Name=state_name).one()
            dis = Districts.query.filter_by(State_Code=state.State_Id).all()
            for district in dis:
                constituency_district = AssemblyConstituency.query.filter_by(District_Code=district.District_Id).all()
                if constituency_district:
                    constituency_list = []

                    for constituency in constituency_district:
                        constituency_dict = {}
                        constituency_dict["Constituency_Id"] = constituency.Constituency_Id
                        constituency_dict["Constituency_Name"] = constituency.Constituency_Name
                        constituency_dict["Constituency_No"] = constituency.Constituency_No
                        constituency_dict["District_Code"] = constituency.District_Code
                        constituency_list.append(constituency_dict)
            return {"constituency": constituency_list}
        
    except:
        return {"message": "No constituency Available"}


@AssemblyConstituency_API_blueprint.route("/admin/add_constituency", methods=["POST"])
def add_constituency():
    body = request.json
    constituency = AssemblyConstituency(
        body["Constituency_Name"],
        body["Constituency_No"],
        body["District_Code"],
    )
    db.session.add(constituency)
    db.session.commit()
    return {"message": "New constituency added successfully"}


@AssemblyConstituency_API_blueprint.route(
    "/admin/delete_constituency", methods=["DELETE"]
)
def constituency_delete():
    body = request.json
    constituency = AssemblyConstituency.query.get(body["Constituency_Id"])
    db.session.delete(constituency)
    db.session.commit()

    return "Constituency was successfully deleted"


# Endpoint for updating a guide
@AssemblyConstituency_API_blueprint.route(
    "/admin/update_constituency", methods=["PUT"]
)
def constituesncy_update():
    body = request.json
    constituency = AssemblyConstituency.query.get(body["Constituency_Id"])
    Constituency_Name = request.json["Constituency_Name"]
    Constituency_No = request.json["Constituency_No"]
    if Constituency_Name:
        constituency.Constituency_Name = Constituency_Name
    if Constituency_No:
        constituency.Constituency_No = Constituency_No
    db.session.commit()
    return "Constituency was successfully updated"
