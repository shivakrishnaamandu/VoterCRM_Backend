USE voter_crm;

CREATE TABLE AssemblyConstituency(
    Constituency_Id int PRIMARY KEY AUTO_INCREMENT,
    Constituency_Name varchar(100) UNIQUE NOT NULL,
    Constituency_No int NOT NULL,
    District_Code int NOT NULL,
    FOREIGN KEY (District_Code) REFERENCES Districts(District_Id)
);


