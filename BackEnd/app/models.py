from voterCRMB import db


class Admins(db.Model):
    __tablename__ = 'admins'

    admin_id = db.Column(db.String(100), primary_key=True)
    user_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, admin_id, user_name, password):
        self.admin_id = admin_id
        self.user_name = user_name
        self.password = password

    def to_dict(self):
        return {
            "adminid": self.admin_id,
            "username": self.user_name,
            "password": self.password
        }

    __tablename__ = 'Agents'

    Agent_Id = db.Column(db.String(100), primary_key=True)
    Username = db.Column(db.String(255), unique=True)
    Hash_Password = db.Column(db.String(255))

    def __init__(self, Agent_Id, Username, Hash_Password):
        self.Agent_Id = Agent_Id
        self.Username = Username
        self.Hash_Password = Hash_Password

    def to_dict(self):
        return {
            "Agent_Id": self.Agent_Id,
            "username": self.user_name,
            "Hash_Password": self.Hash_Password
        }
      
class States(db.Model):
    __tablename__ = 'states'

    state_code = db.Column(db.String(100), primary_key=True)
    state_name = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def __init__(self, state_code, state_name, country):
        self.state_code = state_code
        self.state_name = state_name
        self.country = country
