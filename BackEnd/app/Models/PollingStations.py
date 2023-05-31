from app import db


class PollingStations(db.Model):
    __tablename__ = "PollingStations"

    Polling_Station_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Polling_Station_Name = db.Column(db.String(100), nullable=False)
    Polling_Station_No = db.Column(db.Integer, nullable=False)
    Polling_Station_Location = db.Column(db.String(100))
    Assembly_Constituency_Name = db.Column(
        db.String(100),
        db.ForeignKey("AssemblyConstituency.Constituency_Name"),
        nullable=False,
    )

    def __init__(
        self,
        Polling_Station_Name,
        Polling_Station_No,
        Polling_Station_Location,
        Assembly_Constituency_Name,
    ):
        self.Polling_Station_Name = Polling_Station_Name
        self.Polling_Station_No = Polling_Station_No
        self.Polling_Station_Location = Polling_Station_Location
        self.Assembly_Constituency_Name = Assembly_Constituency_Name
