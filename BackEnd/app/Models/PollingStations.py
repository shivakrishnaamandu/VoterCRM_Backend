from app import db


class PollingStations(db.Model):
    __tablename__ = "PollingStations"

    Polling_Station_Id = db.Column(db.Integer, primary_key=True)
    Polling_Station_Name = db.Column(db.String(100), nullable=False)
    Polling_Station_No = db.Column(db.Integer, nullable=False)
    Polling_Station_Location = db.Column(db.String(100))
    Assembly_Constituency_Code = db.Column(db.Integer,db.ForeignKey("AssemblyConstituency.Constituency_Id"), nullable=False)

    def __init__(self,Polling_Station_Id, Polling_Station_Name, Polling_Station_No,Polling_Station_Location,Assembly_Constituency_Code):
        self.Polling_Station_Id = Polling_Station_Id
        self.Polling_Station_Name = Polling_Station_Name
        self.Polling_Station_No = Polling_Station_No
        self.Polling_Station_Location = Polling_Station_Location
        self.Assembly_Constituency_Code = Assembly_Constituency_Code