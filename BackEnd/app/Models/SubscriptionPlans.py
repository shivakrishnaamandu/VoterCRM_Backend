from app import db


class SubscriptionPlan(db.Model):
    __tablename__ = "SubscriptionPlans"
    Plan_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Plan_Name = db.Column(db.String(25), unique=True, nullable=False)
    Plan_Description = db.Column(db.Text)
    Plan_Duration_Days = db.Column(db.Integer, nullable=False)
    Plan_Cost = db.Column(db.Integer)

    def __init__(self, Plan_Name, Plan_Description, Plan_Duration_Days, Plan_Cost):
        self.Plan_Name = Plan_Name
        self.Plan_Description = Plan_Description
        self.Plan_Duration_Days = Plan_Duration_Days
        self.Plan_Cost = Plan_Cost
