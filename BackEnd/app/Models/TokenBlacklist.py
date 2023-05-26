from app import db
from datetime import datetime


class TokenBlacklist(db.Model):
    __tablename__ = "TokenBlacklist"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    JWT_Token = db.Column(db.String(256), unique=True, nullable=False)
    Expired_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, JWT_Token):
        self.JWT_Token = JWT_Token
