USE voter_crm;

CREATE TABLE AdminCandidateMapping(
     Mapping_Id int PRIMARY KEY AUTO_INCREMENT,
     Admin_Id int NOT NULL,
     FOREIGN KEY (Admin_Id) REFERENCES Agents(Agent_Id),
     Candidate_Id int NOT NULL,
     FOREIGN KEY (Candidate_Id) REFERENCES Candidates(Candidate_Id),
     Assigned_On timestamp DEFAULT CURRENT_TIMESTAMP,
     Assignment_Status varchar(25) NOT NULL,
     Updated_On timestamp ON UPDATE CURRENT_TIMESTAMP

);