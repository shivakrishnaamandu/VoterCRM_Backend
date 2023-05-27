 USE voter_crm;
 
 CREATE TABLE AgentPollingAssignment(
       Assignment_Id int PRIMARY KEY auto_increment,
       Agent_Id int NOT NULL,
       FOREIGN KEY (Agent_Id) REFERENCES Agents(Agent_Id),
       Polling_station_Code int NOT NULL,
       FOREIGN KEY (Polling_station_Code) REFERENCES PollingStations(Polling_Station_Id),
       Candidate_Id int NOT NULL,
       FOREIGN KEY (Candidate_Id) REFERENCES Candidates(Candidate_Id),
       Subscription_Id int NOT NULL,
       FOREIGN KEY (Subscription_Id) REFERENCES Subscriptions(Subscription_Id),
       Assigned_On timestamp DEFAULT CURRENT_TIMESTAMP,
       Assignment_Status varchar(25) NOT NULL,
       Updated_On timestamp ON UPDATE CURRENT_TIMESTAMP
 );