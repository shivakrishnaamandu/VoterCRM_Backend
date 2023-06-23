from app.__init__ import application, db
from app.Models.Candidates import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, jsonify

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)    
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

Candidates_API_blueprint = Blueprint("Candidates_API", __name__)

@Candidates_API_blueprint.route("/admin/candidates_list", methods=["GET"])
def candidate_list():
    candidates = Candidates.query.all()
    if candidates:
        candidates_list = []
        for candidate in candidates:
            candidate_dict = {}
            candidate_dict["Candidate_Id"] = candidate.Candidate_Id
            candidate_dict["Candidate_Name"] = candidate.Candidate_Name
            candidate_dict["Candidate_Age"] = candidate.Candidate_Age
            candidate_dict["Candidate_Gender"] = candidate.Candidate_Gender
            candidate_dict["Candidate_Party"] = candidate.Candidate_Party
            candidate_dict["Candidate_Constituency"] = candidate.Candidate_Constituency
            candidates_list.append(candidate_dict)
        return {"Candidates": candidates_list}
    else:
        return {"message": "No Candidates contesting.."}



@Candidates_API_blueprint.route("/admin/add_candidate", methods=["POST"])
def add_candidate():
    body = request.json
    candidate = Candidates(
        body["Candidate_Name"],
        body["Candidate_Age"],
        body["Candidate_Gender"],
        body["Candidate_Party"],
        body["Candidate_Constituency"]
    )
    db.session.add(candidate)
    db.session.commit()
    return {"message": "New candidate added successfully"}


@Candidates_API_blueprint.route("/admin/delete_candidate", methods=["POST"])
def delete_candidate():
    candidate_name = request.json["Candidate_Name"]
    if(candidate_name==""):
        return {"message": "Candidate name is empty."}
    del_candidate = Candidates.query.filter_by(Candidate_Name=candidate_name).first()
    if del_candidate: 
            db.session.delete(del_candidate)  
            db.session.commit()
            return {"message": "Candidate deleted successfully"}
           
    else:
            return {"message": "Candidate not found"}


@Candidates_API_blueprint.route("/admin/update_candidate", methods=["POST"])
def update_candidate():
    try:
        existing_candidate_name, update_candidate_name,update_candidate_age,update_candidate_gender,update_candidate_party,update_candidate_constituency  = (
            request.json["Existing_Candidate_Name"],
            request.json["Update_Candidate_Name"],
            request.json["Update_Candidate_Age"],
            request.json["Update_Candidate_Gender"],
            request.json["Update_Candidate_Party"],
            request.json["Update_Candidate_Constituency"]

        )
        existing_candidate = Candidates.query.filter_by(Candidate_Name=existing_candidate_name).first()
        if existing_candidate:
            existing_candidate.Candidate_Name = update_candidate_name
            existing_candidate.Candidate_Age = update_candidate_age         
            existing_candidate.Candidate_Gender = update_candidate_gender
            existing_candidate.Candidate_Party = update_candidate_party
            existing_candidate.Candidate_Constituency = update_candidate_constituency            
            db.session.commit()
            db.session.close()
            return {"message": "Candidate details updated successfully."}
        else:
            return {"message": "Candidate Not available"}
    except Exception as e:
        db.session.rollback()
        return jsonify("Error: " + str(e))

    
