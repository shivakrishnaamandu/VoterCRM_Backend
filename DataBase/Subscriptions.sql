USE voter_crm;

CREATE TABLE Subscriptions(
      Subscription_Id int PRIMARY KEY AUTO_INCREMENT,
      Candidate_Id int NOT NULL,
      FOREIGN KEY (Candidate_Id) REFERENCES  Candidates(Candidate_Id),
      Plan_Id int NOT NULL,
      FOREIGN KEY (Plan_Id) REFERENCES SubscriptionPlans(Plan_Id),
      Subscribed_On timestamp DEFAULT CURRENT_TIMESTAMP,
      Subscription_Status varchar(25) NOT NULL,
      Updated_On timestamp ON UPDATE CURRENT_TIMESTAMP
);