from app import db
from datetime import datetime

class AgentPollingAssignment(db.Model):
    
    __tablename__ = "AgentPollingAssignment"

    Assignment_Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Agent_Id = db.Column(db.Integer, db.ForeignKey("Agents.Agent_Id"), nullable = False)
    Polling_Station_Code = db.Column(db.Integer, db.ForeignKey("PollingStations.Polling_Station_Id"), nullable = False)
    Candidate_Id = db.Column(db.Integer, db.ForeignKey("Candidates.Candidate_Id"), nullable = False)
    Subscription_Id = db.Column(db.Integer, db.ForeignKey("Subscriptions.Subscription_Id"), nullable = False)
    Assigned_On = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Assignment_Status =  db.Column(db.String(25), nullable = False)
    Updated_On = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, Agent_Id, Polling_Station_Code, Candidate_Id, Subscription_Id, Assignment_Status):
        self.Agent_Id = Agent_Id
        self.Polling_Station_Code = Polling_Station_Code
        self.Candidate_Id =  Candidate_Id
        self.Subscription_Id = Subscription_Id
        self.Assignment_Status = Assignment_Status  