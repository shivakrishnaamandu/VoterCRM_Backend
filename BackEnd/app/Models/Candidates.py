from app import db

class Candidates(db.Model):
    __tablename__ = "Candidates"

    Candidate_Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Candidate_Name = db.Column(db.String(100), nullable = False)
    Candidate_Age = db.Column(db.Integer, nullable =  False)
    Candidate_Gender = db.Column(db.String(10), nullable = False)
    Candidate_Party = db.Column(db.String(100), db.ForeignKey("PoliticalParties.Party_Name"), nullable = False)
    Candidate_Constituency = db.Column(db.Integer, db.ForeignKey("AssemblyConstituency.Constituency_Id", nullable = False))

    def __init__ (self, Candidate_Id, Candidate_Name, Candidate_Age, Candidate_Gender, Candidate_Party, Candidate_Constituency):
        self.Candidate_Id = Candidate_Id
        self.Candidate_Name = Candidate_Name
        self.Candidate_Age = Candidate_Age
        self.Candidate_Gender = Candidate_Gender
        self.Candidate_Party = Candidate_Party
        self.Candidate_Constituency = Candidate_Constituency