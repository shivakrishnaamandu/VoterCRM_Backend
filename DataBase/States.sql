USE voter_crm;

CREATE TABLE States(
	State_Id int PRIMARY KEY AUTO_INCREMENT,
	State_Name varchar(100) UNIQUE NOT NULL,
	State_No int UNIQUE NOT NULL
);



