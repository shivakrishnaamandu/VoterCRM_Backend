USE voter_crm;

CREATE TABLE PollingStations(
    Polling_Station_Id int UNIQUE KEY AUTO_INCREMENT,
    Polling_Station_Name varchar(100) NOT NULL,
    Polling_Station_No int NOT NULL,
    Polling_Station_Location varchar(150),
    Assembly_Constituency_Name varchar(100) NOT NULL,
    Constraint PK_Polling Primary KEY (Assembly_Constituency_Name, Polling_Station_No),
    Constraint Unique_Polling UNIQUE KEY (Polling_Station_No,  Polling_Station_Name ),
    FOREIGN KEY (Assembly_Constituency_Name) REFERENCES AssemblyConstituency(Constituency_Name)
);
