USE voter_crm;

CREATE TABLE Candidates(
    Candidate_Id int PRIMARY KEY AUTO_INCREMENT,
    Candidate_Name varchar(100) NOT NULL,
    Candidate_Age int NOT NULL,
    Candidate_Gender varchar(10) NOT NULL,
    Candidate_Party varchar(100) NOT NULL,
	FOREIGN KEY (Candidate_Party) REFERENCES PoliticalParties(Party_Name),
    Candidate_Constituency int NOT NULL,
    FOREIGN KEY (Candidate_Constituency) REFERENCES AssemblyConstituency(Constituency_Id)
);
