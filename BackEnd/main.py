from app import application, db
from app.APIs.Admin_Auth_API import Admin_Auth_API_blueprint
from app.APIs.States_API import States_API_blueprint
from app.APIs.Districts_API import Districts_API_blueprint
from app.APIs.Voters_API import Voters_API_blueprint
from app.APIs.AssemblyConstituency_API import AssemblyConstituency_API_blueprint
from app.APIs.PollingStation_API import PollingStation_API_blueprint
from app.APIs.Agents_API import Agents_API_blueprint
from app.APIs.Analytics_API import Analytics_API_blueprint
from app.APIs.AgentPollingAssignment_API import AgentPollingAssignemnt_API_blueprint
from app.APIs.PoliticalParties_API import PoliticalParties_API_blueprint
from app.APIs.Candidates_API import Candidates_API_blueprint
from app.APIs.Subscriptions_API import Subscriptions_API_blueprint
from app.Models import *
from flask import request
import traceback

application.register_blueprint(Admin_Auth_API_blueprint)
application.register_blueprint(States_API_blueprint)
application.register_blueprint(Districts_API_blueprint)
application.register_blueprint(Voters_API_blueprint)
application.register_blueprint(AssemblyConstituency_API_blueprint)
application.register_blueprint(PollingStation_API_blueprint)
application.register_blueprint(Agents_API_blueprint)
application.register_blueprint(AgentPollingAssignemnt_API_blueprint)
application.register_blueprint(Analytics_API_blueprint)
application.register_blueprint(PoliticalParties_API_blueprint)
application.register_blueprint(Candidates_API_blueprint)
application.register_blueprint(Subscriptions_API_blueprint)

if __name__ == "__main__":
    with application.app_context():
        print("Importing and adding tables")
        # TODO : Remove this try block once the DB is integrated
        try:
            from app.Models import *

            db.create_all()  # Create sql tables for our data models
            print("tables created")
        except:
            print("Excpetion while connecting to DB in application main run")
            print(traceback.print_exc())

        application.run(host="0.0.0.0", debug=True, port=8000)
