from app import db


class Subscription(db.Model):
    __tablename__ = "Subscriptions"
    Subscription_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Candidate_Id = db.Column(
        db.Integer, db.ForeignKey("Candidates.Candidate_Id"), nullable=False
    )
    Plan_Id = db.Column(
        db.Integer, db.ForeignKey("SubscriptionPlans.Plan_Id"), nullable=False
    )
    Subscribed_On = db.Column(
        db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp()
    )
    Subscription_Status = db.Column(db.String(25), nullable=False)
    Updated_On = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    def __init__(self, Candidate_Id, Plan_Id, Subscription_Status):
        self.Candidate_Id = Candidate_Id
        self.Plan_Id = Plan_Id
        self.Subscription_Status = Subscription_Status
