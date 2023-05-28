USE voter_crm;

CREATE TABLE Logins(
      Id int PRIMARY KEY auto_increment,
      User_Id int NOT NULL,
      IP_Address varchar(25) NOT NULL,
      Device varchar(50) NOT NULL,
      Token text NOT NULL,
      Created_On timestamp DEFAULT CURRENT_TIMESTAMP,
      Status varchar(25),
      Updated_On timestamp ON UPDATE CURRENT_TIMESTAMP,
      FOREIGN KEY (User_Id) REFERENCES Agents(Agent_Id)
);