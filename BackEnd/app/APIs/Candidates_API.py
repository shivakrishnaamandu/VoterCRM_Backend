from app.__init__ import application, db
from app.Models.Candidates import *
from app.Models.Logins import *
from app.Models.AdminCandidateMapping import *
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

    # getting admin_id from token
    token = request.headers["token"]
    login = Logins.query.filter_by(Token = token).first()
    admin_id = login.User_Id

    # getting candidate_id from Candidates table
    candidate = Candidates.query.filter_by(Candidate_Name = body["Candidate_Name"]).first()
    candidate_id = candidate.Candidate_Id

    admincandidatemap = AdminCandidateMapping(admin_id,candidate_id,"Assigned")

    # adding the mapping to the admin-candidate mapping table
    db.session.add(admincandidatemap)
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



    
