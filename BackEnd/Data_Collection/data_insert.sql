create database voter_crm;

use voter_crm;

INSERT INTO States (State_Id, State_Name, State_No) VALUES (1, 'Andhra Pradesh', 1);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (2, 'Arunachal Pradesh', 2);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (3, 'Assam', 3);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (4, 'Bihar', 4);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (5, 'Chhattisgarh', 5);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (6, 'Goa', 6);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (7, 'Gujarat', 7);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (8, 'Haryana', 8);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (9, 'Himachal Pradesh', 9);
INSERT INTO States (State_Id, State_Name, State_No) VALUES (10, 'Jharkhand', 10);


INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (1, 'Anantapur', 1, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (2, 'Chittoor', 2, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (3, 'East Godavari', 3, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (4, 'Guntur', 4, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (5, 'Krishna', 5, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (6, 'Kurnool', 6, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (7, 'Nellore', 7, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (8, 'Prakasam', 8, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (9, 'Srikakulam', 9, 1);
INSERT INTO Districts (District_Id, District_Name, District_No, State_Code) VALUES (10, 'Visakhapatnam', 10, 1);

INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (1, 'Constituency A', 1, 1);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (2, 'Constituency B', 2, 1);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (3, 'Constituency C', 3, 1);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (4, 'Constituency D', 4, 2);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (5, 'Constituency E', 5, 2);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (6, 'Constituency F', 6, 2);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (7, 'Constituency G', 7, 3);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (8, 'Constituency H', 8, 3);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (9, 'Constituency I', 9, 4);
INSERT INTO AssemblyConstituency (Constituency_Id, Constituency_Name, Constituency_No, District_Code) VALUES (10, 'Constituency J', 10, 4);


INSERT INTO PollingStations (Polling_Station_Id, Polling_Station_Name, Polling_Station_No, Polling_Station_Location, Assembly_Constituency_Name) VALUES (1, 'Polling Station A', 1, 'Location A', 'Constituency A');
INSERT INTO PollingStations (Polling_Station_Id, Polling_Station_Name, Polling_Station_No, Polling_Station_Location, Assembly_Constituency_Name) VALUES (2, 'Polling Station B', 2, 'Location B', 'Constituency A');
INSERT INTO PollingStations (Polling_Station_Id, Polling_Station_Name, Polling_Station_No, Polling_Station_Location, Assembly_Constituency_Name) VALUES (3, 'Polling Station C', 3, 'Location C', 'Constituency A');
INSERT INTO PollingStations (Polling_Station_Id, Polling_Station_Name, Polling_Station_No, Polling_Station_Location, Assembly_Constituency_Name) VALUES (4, 'Polling Station D', 4, 'Location D', 'Constituency A');
INSERT INTO PollingStations (Polling_Station_Id, Polling_Station_Name, Polling_Station_No, Polling_Station_Location, Assembly_Constituency_Name) VALUES (5, 'Polling Station E', 5, 'Location E', 'Constituency A');

INSERT INTO PoliticalParties (Party_Id, Party_Name, Party_Symbol, Party_Status, Party_State, Party_President) VALUES (1, 'Party A', 'Symbol A', 'Active', 1, 'President A');
INSERT INTO PoliticalParties (Party_Id, Party_Name, Party_Symbol, Party_Status, Party_State, Party_President) VALUES (2, 'Party B', 'Symbol B', 'Active', 2, 'President B');
INSERT INTO PoliticalParties (Party_Id, Party_Name, Party_Symbol, Party_Status, Party_State, Party_President) VALUES (3, 'Party C', 'Symbol C', 'Active', 3, 'President C');
INSERT INTO PoliticalParties (Party_Id, Party_Name, Party_Symbol, Party_Status, Party_State, Party_President) VALUES (4, 'Party D', 'Symbol D', 'Active', 4, 'President D');
INSERT INTO PoliticalParties (Party_Id, Party_Name, Party_Symbol, Party_Status, Party_State, Party_President) VALUES (5, 'Party E', 'Symbol E', 'Active', 5, 'President E');

INSERT INTO Candidates (Candidate_Id, Candidate_Name, Candidate_Age, Candidate_Gender, Candidate_Party, Candidate_Constituency) VALUES (1, 'Candidate A', 35, 'Male', 'Party A', 1);
INSERT INTO Candidates (Candidate_Id, Candidate_Name, Candidate_Age, Candidate_Gender, Candidate_Party, Candidate_Constituency) VALUES (2, 'Candidate B', 42, 'Female', 'Party B', 2);
INSERT INTO Candidates (Candidate_Id, Candidate_Name, Candidate_Age, Candidate_Gender, Candidate_Party, Candidate_Constituency) VALUES (3, 'Candidate C', 28, 'Male', 'Party C', 1);
INSERT INTO Candidates (Candidate_Id, Candidate_Name, Candidate_Age, Candidate_Gender, Candidate_Party, Candidate_Constituency) VALUES (4, 'Candidate D', 39, 'Female', 'Party A', 3);
INSERT INTO Candidates (Candidate_Id, Candidate_Name, Candidate_Age, Candidate_Gender, Candidate_Party, Candidate_Constituency) VALUES (5, 'Candidate E', 45, 'Male', 'Party B', 3);

INSERT INTO SubscriptionPlans (Plan_Id, Plan_Name, Plan_Description, Plan_Duration_Days, Plan_Cost) VALUES (1, 'Basic', 'Basic plan for beginners', 30, 10);
INSERT INTO SubscriptionPlans (Plan_Id, Plan_Name, Plan_Description, Plan_Duration_Days, Plan_Cost) VALUES (2, 'Standard', 'Standard plan for intermediate users', 60, 20);
INSERT INTO SubscriptionPlans (Plan_Id, Plan_Name, Plan_Description, Plan_Duration_Days, Plan_Cost) VALUES (3, 'Premium', 'Premium plan for advanced users', 90, 30);

INSERT INTO Subscriptions (Subscription_Id, Candidate_Id, Plan_Id, Subscription_Status) VALUES (1, 1, 1, 'Active');
INSERT INTO Subscriptions (Subscription_Id, Candidate_Id, Plan_Id, Subscription_Status) VALUES (2, 2, 2, 'Active');
INSERT INTO Subscriptions (Subscription_Id, Candidate_Id, Plan_Id, Subscription_Status) VALUES (3, 3, 3, 'Active');

-- INSERT INTO Agents (Agent_Id, First_name, Last_name, Username, Hash_Password, Email_Id, IsAdmin, Gender, Phone_No, Address)
-- VALUES (1, 'John', 'Doe', 'johndoe', '123456789', 'exampleemail@example.com', 1, 'Male', '1234567890', '123 Main St');
-- INSERT INTO Agents (Agent_Id, First_name, Last_name, Username, Hash_Password, Email_Id, IsAdmin, Gender, Phone_No, Address)
-- VALUES (2, 'reshma', 'kandula', 'reshma', '12345', 'reshma@example.com', 1, 'Female', '78985555', '123 elm St');

INSERT INTO AdminCandidateMapping (Mapping_Id, Admin_Id, Candidate_Id, Assignment_Status) VALUES (1, 1, 1, 'Assigned');
INSERT INTO AdminCandidateMapping (Mapping_Id, Admin_Id, Candidate_Id, Assignment_Status) VALUES (2, 2, 2, 'Assigned');

INSERT INTO Relations(Relation_Id,Relation_Name) VALUES (1,"Father"),(2,"Husband"),(3,"Mother"),(4,"Wife"),(5,"Other"),(6,"Guru");

