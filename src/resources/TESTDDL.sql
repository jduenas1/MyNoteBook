#CREATE SCHEMA IF NOT EXISTS Test1;
drop table if exists PersonData;
drop table if exists Person;
drop table if exists PWManager;
drop table if exists URLManager;



CREATE TABLE IF NOT EXISTS Person(
ID INT auto_increment,
user_login varchar(255) unique not null,
user_password varchar(255) not null,
first_name varchar (255),
last_name varchar (255),
primary key (ID)
);
 
CREATE TABLE IF NOT EXISTS PWManager(
ID int auto_increment,
passwrd varchar(255),
accnt varchar(255) ,
descprtion varchar(255),
URL varchar(255),
primary key (ID)
);

CREATE TABLE IF NOT EXISTS URLMANAGER(
ID int auto_increment,
url varchar(255),
descprtion varchar (255),
primary key (ID)
);

CREATE TABLE IF NOT EXISTS PersonData(
ID int auto_increment,
PersonID int,
PWManagerID int,
URLManagerID int,
CONSTRAINT fkPerson FOREIGN KEY (PersonID)
references Person(ID),
CONSTRAINT fkPWManager FOREIGN KEY (PWManagerID)
references PWManager(ID),
CONSTRAINT fkURLManager FOREIGN KEY (URLManagerID)
references URLManager(ID),
primary key (ID)
);
