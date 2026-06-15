CREATE DATABASE Immigrant;
USE Immigrant;

CREATE TABLE Immigrant_Table (
	Immigrant_ID INT primary key AUTO_INCREMENT NOT NULL,
    First_Name VARCHAR(40) NOT NULL,
    Last_Name VARCHAR(40) NOT NULL,
    Age INT NOT NULL,
    Sex ENUM('Male', 'Female') NOT NULL,
    Visa ENUM('Student', 'Work', 'Tourist') NOT NULL,
    ReasonOfTravel ENUM('Work', 'School', 'Touring', 'Chaperone'),
    Address VARCHAR(100) NOT NULL
);

CREATE TABLE City_Table(
	City_ID VARCHAR(6) primary key NOT NULL,
    City_Name VARCHAR(70) NOT NULL,
    State_Name VARCHAR(30)
);

CREATE TABLE School_Table(
	School_ID VARCHAR(10) primary key NOT NULL,
    School_Name VARCHAR(150) NOT NULL,
    City_ID VARCHAR(6),
	Address VARCHAR(100) NOT NULL,
    FOREIGN KEY (City_ID) REFERENCES City_Table(City_ID)
);

CREATE TABLE Guardian_Table(
	Immigrant_ID INT Primary key,
	Email VARCHAR(60) UNIQUE NOT NULL,
    No_Children INT NOT NULL,
    Relationship ENUM('Family', 'Teacher', 'Foster', 'Court Appointed', 'Chaperone'),
    FOREIGN KEY(Immigrant_ID) REFERENCES Immigrant_Table(Immigrant_ID)
);
CREATE TABLE Child_Student(
	Immigrant_ID INT primary key,
    Guardian_ID INT,
    School_ID VARCHAR(10),
    FOREIGN KEY (Immigrant_ID) REFERENCES Immigrant_Table(Immigrant_ID),
    FOREIGN KEY (School_ID) REFERENCES School_Table(School_ID),
    FOREIGN KEY (Guardian_ID) REFERENCES Guardian_Table(Immigrant_ID)
);

CREATE TABLE Adult_Student(
	Immigrant_ID INT primary key,
    School_ID VARCHAR(10),
	Email VARCHAR(60) UNIQUE NOT NULL,
    FOREIGN KEY (Immigrant_ID) REFERENCES Immigrant_Table(Immigrant_ID),
    FOREIGN KEY (School_ID) REFERENCES School_Table(School_ID)
);

SHOW Tables;
INSERT INTO City_Table(City_ID, City_Name, State_Name) 
VALUES ("CHZSCH", "Chemitz", "Saxony"),
("KLHBWG", "Karlsruhe", "Baden-Württenburg"),
("BERBER", "Berlin", "Berlin"),
("DRSSCH", "Dresden", "Saxony"),
("MITSCH", "Mittweida", "Saxony"),
("LPZSCH", "Leipzig", "Saxony"),
("HAMHAM", "Hamburg", "Hamburg"),
("HAMHAM", "Hamburg", "Hamburg"),
("FRIBWG", "Freiburg im Breisgua", "Baden-Würtenburg"),
("HNNNSY", "Hannover", "Lower-Saxony"),
("COBBYN", "Coburg", "Bavaria"),
("ZTTSCH", "Zittau", "Saxony"),
("NRDTUR", "Nordhaus", "Thuringia"),
("KOESAT", "Köthen", "Saxony-Anhalt"),
("STGBWG", "Stuttgard", "Baden-Württenburg"),
("KLTRHP", "Kaiserlauten", "Rheinland-Platz");