from app import db
from datetime import datetime


class Logins(db.Model):
    __tablename__ = "Logins"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_Id = db.Column(db.Integer, db.ForeignKey("Agents.Agent_Id"), nullable=False)
    IP_Address = db.Column(db.String(25), nullable=False)
    Device = db.Column(db.String(50), nullable=False)
    Token = db.Column(db.String(256), nullable=False)
    Created_On = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Status = db.Column(db.String(25))
    Updated_On = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, User_Id, IP_Address, Device,Token, Status):
        self.User_Id = User_Id
        self.IP_Address = IP_Address
        self.Device = Device
        self.Token = Token
        self.Status = Status
