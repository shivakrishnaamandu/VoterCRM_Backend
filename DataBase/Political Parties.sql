USE voter_crm;

CREATE TABLE PoliticalParties(
	Party_Id int PRIMARY KEY AUTO_INCREMENT,
	Party_Name varchar(100) UNIQUE NOT NULL,
	Party_Symbol varchar(100) UNIQUE NOT NULL,
	Party_Status varchar(20) NOT NULL,
	Party_State int,
	FOREIGN KEY (Party_State) REFERENCES States(State_Id),
	Party_President varchar(100)
);