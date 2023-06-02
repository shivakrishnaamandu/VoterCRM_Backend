from app import db

class PoliticalParties(db.Model):
    __tablename__ =  "PoliticalParties"

    Party_Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Party_Name = db.Column(db.String(100), unique =  True, nullable = False)
    Party_Symbol = db.Column(db.String(100), unique = True, nullable = False)
    Party_Status =  db.Column(db.String(20), nullable = False)
    Party_State =  db.Column(db.Integer, db.ForeignKey("States.State_Id"))
    Party_President = db.Column(db.String(100))

    def __init__(self, Party_Id, Party_Name, Party_Symbol, Party_Status, Party_State, Party_President):
        self.Party_Id = Party_Id
        self.Party_Name = Party_Name
        self.Party_Symbol = Party_Symbol
        self.Party_State = Party_State
        self.Party_President = Party_President