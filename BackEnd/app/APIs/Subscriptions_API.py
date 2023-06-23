from app.__init__ import application, db
from app.Models.Subscriptions import *
from app.Authentication.jwtservice import JWTService
from app.Authentication.middleware import Middleware
from flask import request, Blueprint,jsonify

jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)    
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

Subscriptions_API_blueprint = Blueprint("Subscriptions_API", __name__)

@Subscriptions_API_blueprint.route("/admin/subscriptions_list", methods=["GET"])
def subscription_list():
    subscriptions = Subscriptions.query.all()
    if subscriptions:
        subscriptions_list = []
        for subscription in subscriptions:
            subscription_dict = {}
            subscription_dict["Subscription_Id"] = subscription.Subscription_Id
            subscription_dict["Candidate_Id"] = subscription.Candidate_Id
            subscription_dict["Plan_Id"] = subscription.Plan_Id
            subscription_dict["Subscribed_On"] = subscription.Subscribed_On
            subscription_dict["Subscription_Status"] = subscription.Subscription_Status
            subscription_dict["Updated_On"] = subscription.Updated_On
            subscriptions_list.append(subscription_dict)
        return {"Subscriptions": subscriptions_list}
    else:
        return {"message": "No Subscriptions available.."}



@Subscriptions_API_blueprint.route("/admin/add_subscription", methods=["POST"])
def add_subscription():
    body = request.json
    subscription = Subscriptions(
        body["Candidate_Id"],
        body["Plan_Id"],
        body["Subscription_Status"]        
    )
    db.session.add(subscription)
    db.session.commit()
    return {"message": "New subscription added successfully"}


@Subscriptions_API_blueprint.route("/admin/delete_subscription", methods=["POST"])
def delete_subscription():
    candidate_id = request.json["Candidate_Id"]
    plan_id = request.json["Plan_Id"]
    if(candidate_id == "" or plan_id == ""):
        return {"message": "Subscription is not available."}
    del_candidate = Subscriptions.query.filter_by(Candidate_Id=candidate_id,Plan_Id=plan_id).first()
    if del_candidate: 
            db.session.delete(del_candidate) 
            db.session.commit()
            return {"message": "Subscription deleted successfully"}
           
    else:
            return {"message": "Subscription not found"}

@Subscriptions_API_blueprint.route("/admin/update_subscription", methods=["POST"])
def update_subscription():
    try:
        existing_candidate_id, existing_plan_id,update_candidate_id,update_plan_id,update_subscription_status = (
            request.json["Existing_Candidate_Id"],
            request.json["Existing_Plan_Id"],
            request.json["Update_Candidate_Id"],
            request.json["Update_Plan_Id"],
            request.json["Update_Subscription_Status"]
            )
        existing_subscription = Subscriptions.query.filter_by(Candidate_Id=existing_candidate_id,
                                                        Plan_Id=existing_plan_id).first()
        if existing_subscription:
            existing_subscription.Candidate_Id = update_candidate_id
            existing_subscription.Plan_Id = update_plan_id         
            existing_subscription.Subscription_Status = update_subscription_status
            db.session.commit()
            db.session.close()
            return {"message": "Subscription details updated successfully."}
        else:
            return {"message": "Subscription not available"}
    except Exception as e:
        db.session.rollback()
        return jsonify("Error: " + str(e))

    
