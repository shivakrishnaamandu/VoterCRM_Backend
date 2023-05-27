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
    Polling_Station_Code int NOT NULL,
    FOREIGN KEY (Relation_Type) REFERENCES Relations(Relation_Id),
    FOREIGN KEY (Polling_Station_Code) REFERENCES PollingStations(Polling_Station_Id)
);


