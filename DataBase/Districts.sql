USE voter_crm;

CREATE TABLE Districts(
    District_Id int PRIMARY KEY AUTO_INCREMENT,
    District_Name varchar(100) UNIQUE NOT NULL,
    District_No int NOT NULL,
    State_Code int NOT NULL,
    FOREIGN KEY (State_Code) REFERENCES States(State_Id)
);

