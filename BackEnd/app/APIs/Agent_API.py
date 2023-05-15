from Backend.app import application, db
from Backend.app.Models.Agents import Agents
from Backend.app.Models.TokenBlacklist import TokenBlacklist
from Backend.app.Authentication.jwtservice import JWTService
from Backend.app.Authentication.middleware import Middleware
from Backend.app.Authentication.hashingservice import HashingService
from flask import request, Blueprint, redirect, url_for
from werkzeug import exceptions
import uuid

sign_up_key = "signupkey"
jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)
hashing_service = HashingService()

application.before_request(lambda: middleware.auth(request))

Agent_API_blueprint = Blueprint("Agent_API", __name__)


@AgentAPI_blueprint.route("/agent/auth/login", methods=["POST"])
def log_in():
    username, password = request.json["Username"], request.json["Password"]
    agent = Agents.query.filter_by(Username=username, IsAdmin=False).first()
    if agent is None:
        return exceptions.Unauthorized(
            description="Incorrect username/password combination"
        )
    is_password_correct = hashing_service.check_bcrypt(
        password.encode("utf-8"), admin.Hash_Password.encode("utf-8")
    )

    if not is_password_correct:
        return exceptions.Unauthorized(
            description="Incorrect username/password combination"
        )
    token_payload = {"username": username}
    token = jwt_service.generate(token_payload)

    if token is None:
        return exceptions.InternalServerError(description="Login Failed")
    return {"token": token}


@Agent_API_blueprint.route("/agent/auth/is_logged_in")
def is_logged_in():
    return {"message": "token is valid"}


@Agent_API_blueprint.route("/agent/auth/logout")
def log_out():
    token = request.headers["token"]
    tokenblacklist = TokenBlacklist(token)
    db.session.add(tokenblacklist)
    db.session.commit()
    return {"message": "Logged out successfully"}
