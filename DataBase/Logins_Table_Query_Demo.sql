/* Execute each query individually one after another in the same order */

CREATE DATABASE TRIALS;

use trials;

drop table Logins;

CREATE TABLE Logins(
      Id int PRIMARY KEY auto_increment,
      User_Id int NOT NULL,
      IP_Address varchar(25) NOT NULL,
      Device varchar(50) NOT NULL,
      Token text NOT NULL,
      Created_On timestamp DEFAULT CURRENT_TIMESTAMP,
      Status varchar(25),
      Updated_On timestamp ON UPDATE CURRENT_TIMESTAMP 
);

select * from Logins;

insert into Logins(User_Id, IP_Address, Device, Token, status) values(515, 190.250, 'laptop', 'qgekabsjdvckuwahf', 'logged_in');

select * from Logins;

UPDATE Logins SET status = 'logged_out' WHERE User_Id = 515;

select * from Logins;

insert into Logins(User_Id, IP_Address, Device, Token, status) values(530, 1987.209, 'mobile', '.kjs.nfzc.kj', 'logged_in');

select * from Logins;