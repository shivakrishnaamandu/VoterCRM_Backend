from app import db


class Voters(db.Model):
    __tablename__ = "Voters"

    Voter_Row_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Voter_UID = db.Column(db.String(10), unique=True)
    Voter_Name = db.Column(db.String(100), nullable=False)
    Relative_Name = db.Column(db.String(100), nullable=False)
    Relation_Type = db.Column(
        db.Integer, db.ForeignKey("Relations.Relation_Id"), nullable=False
    )
    House_Number = db.Column(db.Text, nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Assembly_Constituency_Name = db.Column(db.String(100), nullable=False)
    Polling_Station_No = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        Voter_UID,
        Voter_Name,
        Relative_Name,
        Relation_Type,
        House_Number,
        Age,
        Gender,
        Assembly_Constituency_Name,
        Polling_Station_No,
    ):
        self.Voter_UID = Voter_UID
        self.Voter_Name = Voter_Name
        self.Relative_Name = Relative_Name
        self.Relation_Type = Relation_Type
        self.House_Number = House_Number
        self.Age = Age
        self.Gender = Gender
        self.Assembly_Constituency_Name = Assembly_Constituency_Name
        self.Polling_Station_No = Polling_Station_No
