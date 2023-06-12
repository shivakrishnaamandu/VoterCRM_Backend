from app import db
from app.Models.Agents import *
from app.Models.Candidates import *


class AdminCandidateMapping(db.Model):
    __tablename__ = "AdminCandidateMapping"

    Mapping_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Admin_Id = db.Column(db.Integer, db.ForeignKey("Agents.Agent_Id"), nullable=False)
    Candidate_Id = db.Column(
        db.Integer, db.ForeignKey("Candidates.Candidate_Id"), nullable=False
    )
    Assigned_On = db.Column(
        db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp()
    )
    Assignment_Status = db.Column(db.String(25), nullable=False)
    Updated_On = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    def __init__(self, Admin_Id, Candidate_Id, Assignment_Status):
        self.Admin_Id = Admin_Id
        self.Candidate_Id = Candidate_Id
        self.Assignment_Status = Assignment_Status


"""
CREATE TABLE AdminCandidateMapping(
     Mapping_Id int PRIMARY KEY AUTO_INCREMENT,
     Admin_Id int NOT NULL,
     FOREIGN KEY (Admin_Id) REFERENCES Agents(Agent_Id),
     Candidate_Id int NOT NULL,
     FOREIGN KEY (Candidate_Id) REFERENCES Candidates(Candidate_Id),
     Assigned_On timestamp DEFAULT CURRENT_TIMESTAMP,
     Assignment_Status varchar(25) NOT NULL,
     Updated_On timestamp ON UPDATE CURRENT_TIMESTAMP

);
"""
