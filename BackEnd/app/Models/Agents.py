from app import db


class Agents(db.Model):
    __tablename__ = "Agents"

    Agent_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_name = db.Column(db.String(50), nullable=False)
    Last_name = db.Column(db.String(50), nullable=False)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Hash_Password = db.Column(db.String(256), nullable=False)
    Email_Id = db.Column(db.String(100), unique=True)
    IsAdmin = db.Column(db.Boolean, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Phone_No = db.Column(db.String(10))
    Address = db.Column(db.Text)

    def __init__(
        self,
        First_name,
        Last_name,
        Username,
        Hash_Password,
        Email_Id,
        IsAdmin,
        Gender,
        Phone_No=None,
        Address=None,
    ):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Username = Username
        self.Hash_Password = Hash_Password
        self.Email_Id = Email_Id
        self.IsAdmin = IsAdmin
        self.Gender = Gender
        self.Phone_No = Phone_No
        self.Address = Address
