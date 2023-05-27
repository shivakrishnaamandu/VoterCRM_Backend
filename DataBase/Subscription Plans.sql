USE voter_crm;

CREATE TABLE SubscriptionPlans(
     Plan_Id int PRIMARY KEY AUTO_INCREMENT,
     Plan_Name varchar(25) UNIQUE NOT NULL,
     Plan_Description text,
     Plan_Duration_Days int NOT NULL,
     Plan_Cost int
);