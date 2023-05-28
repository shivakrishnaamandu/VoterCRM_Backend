from app import db


class States(db.Model):
    __tablename__ = "States"

    State_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    State_Name = db.Column(db.String(50), unique=True)
    State_No = db.Column(db.Integer)

    def __init__(self, State_Name, State_No):
        self.State_Name = State_Name
        self.State_No = State_No
