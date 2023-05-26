from app import db


class Relations(db.Model):
    __tablename__ = "Relations"

    Relation_Id = db.Column(db.Integer, primary_key=True)
    Relation_Name = db.Column(db.String(50), unique=True)

    def __init__(self, Relation_ID, Relation_Name):
        self.Relation_ID = Relation_ID
        self.Relation_Name = Relation_Name