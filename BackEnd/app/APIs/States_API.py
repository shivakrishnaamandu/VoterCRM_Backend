from app.__init__ import application, db
from app.Models.States import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint
import uuid

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

States_API_blueprint = Blueprint("States_API", __name__)


@States_API_blueprint.route("/admin/states")
def get_all_states():
    print(f"url accessed")
    states = States.query.all()
    if states:
        state_list = []
        for state in states:
            print(f"State Name: {state.State_Name}")
            state_dict = {}
            state_dict["State_Id"] = state.State_Id
            state_dict["State_Name"] = state.State_Name
            state_dict["State_No"] = state.State_No
            state_list.append(state_dict)
        return {"states": state_list}
    else:
        return {"message": "No states Available"}


@States_API_blueprint.route("/admin/add_state", methods=["POST"])
def add_state():
    body = request.json
    state = States(body["State_Name"], body["State_No"])
    db.session.add(state)
    db.session.commit()
    return {"message": "New state added successfully"}


@States_API_blueprint.route("/admin/delete_state", methods=["POST"])
def delete_state():
    state_name = request.json["State_Name"]
    try:
        States.query.filter_by(State_Name=state_name).delete()  # Fetching the instance
        db.session.commit()
        return {"message": "State deleted successfully"}
    except:
        return {"message": "Error deleting state"}


@States_API_blueprint.route("/admin/update_state", methods=["POST"])
# Can update State_Name 
def update_state():
    try:
        existing_state_name, Update_State_name = (
            request.json["Existing_State_Name"],
            request.json["Update_State_Name"],
            #request.json["Update_State_No"]
        )
        existing_state = States.query.filter_by(State_Name=existing_state_name).first()
        if existing_state:
            existing_state.State_Name = Update_State_name
            #existing_state.State_No = Updated_State_no
            db.session.commit()
            db.session.close()
            return {"message": "State updated successfully"}
        else:
            return {"message": "State Not available"}
    except Exception as e:
        db.session.rollback()
        return {"Error: " + str(e)}
    
