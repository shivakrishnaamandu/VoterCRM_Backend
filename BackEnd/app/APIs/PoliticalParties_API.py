from app.__init__ import application, db
from app.Models.PoliticalParties import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint, jsonify

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

PoliticalParties_API_blueprint = Blueprint("PoliticalParties_API", __name__)

@PoliticalParties_API_blueprint.route("/admin/politicalparties_list", methods=["GET"])
def politicalparties_list():
    politicalparties = PoliticalParties.query.all()
    if politicalparties:
        politicalparties_list = []
        for party in politicalparties:
            party_dict = {}
            party_dict["Party_Id"] = party.Party_Id
            party_dict["Party_Name"] = party.Party_Name
            party_dict["Party_Symbol"] = party.Party_Symbol
            party_dict["Party_Status"] = party.Party_Status
            party_dict["Party_State"] = party.Party_State
            party_dict["Party_President"] = party.Party_President
            politicalparties_list.append(party_dict)
        return {"Political Parties": politicalparties_list}
    else:
        return {"message": "No Political Parties Available"}



@PoliticalParties_API_blueprint.route("/admin/add_politicalparty", methods=["POST"])
def add_politicalparty():
    body = request.json
    party= PoliticalParties(
        body["Party_Name"],
        body["Party_Symbol"],
        body["Party_Status"],
        body["Party_State"],
        body["Party_President"]
    )
    db.session.add(party)
    db.session.commit()
    return {"message": "New Political party added successfully"}


@PoliticalParties_API_blueprint.route("/admin/delete_politicalparty", methods=["POST"])
def delete_politicalparty():
    party_name = request.json["Party_Name"]
    if(party_name==""):
        return {"message": "Party name is empty."}
    del_party = PoliticalParties.query.filter_by(Party_Name=party_name).first()
    if del_party: 
            db.session.delete(del_party)  
            db.session.commit()
            return {"message": "Political party deleted successfully"}
           
    else:
            return {"message": "Political party not found"}


@PoliticalParties_API_blueprint.route("/admin/update_politicalparty", methods=["POST"])
def update_politicalparty():
    try:
        existing_party_name, update_party_name,update_party_symbol,update_party_status,update_party_state,update_party_president  = (
            request.json["Existing_Party_Name"],
            request.json["Update_Party_Name"],
            request.json["Update_Party_Symbol"],
            request.json["Update_Party_Status"],
            request.json["Update_Party_State"],
            request.json["Update_Party_President"]
        )
        existing_party = PoliticalParties.query.filter_by(Party_Name=existing_party_name).first()
        if existing_party:
            existing_party.Party_Name = update_party_name
            existing_party.Party_Symbol = update_party_symbol            
            existing_party.Party_Status = update_party_status
            existing_party.Party_State = update_party_state
            existing_party.Party_President = update_party_president            
            db.session.commit()
            db.session.close()
            return {"message": "Political Party details updated successfully"}
        else:
            return {"message": "Political Party Not available"}
    except Exception as e:
        db.session.rollback()
        return jsonify("Error: " + str(e))

    
