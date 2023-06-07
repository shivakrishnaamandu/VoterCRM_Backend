USE voter_crm;

CREATE TABLE Voters(
    Voter_Row_ID int PRIMARY KEY AUTO_INCREMENT,
    Voter_UID char(10) UNIQUE NOT NULL,
    Voter_Name varchar(100) NOT NULL,
    Relative_Name VARCHAR(100) NOT NULL,
    Relation_Type int NOT NULL,
    House_Number text NOT NULL,
    Age int NOT NULL,
    Gender varchar(10) NOT NULL,
    Assembly_Constituency_Name varchar(100) NOT NULL,
    Polling_Station_No int NOT NULL,
    FOREIGN KEY (Relation_Type) REFERENCES Relations(Relation_Id),
    CONSTRAINT FK_Polling FOREIGN KEY (Assembly_Constituency_Name, Polling_Station_No)
    REFERENCES PollingStations(Assembly_Constituency_Name, Polling_Station_No)
);


