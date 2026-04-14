CREATE DATABASE School;

USE School;

CREATE TABLE Students (
    Student_id INT PRIMARY KEY AUTO_INCREMENT,
    Fname VARCHAR(100) NOT NULL,
    Sname VARCHAR(100) NOT NULL,
    Date_of_birth DATE,
    Sex ENUM('Male', 'Female') NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(100) UNIQUE,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Staff (
    Staff_id INT PRIMARY KEY AUTO_INCREMENT,
    Fname VARCHAR(100) NOT NULL,
    Sname VARCHAR(100) NOT NULL,
    Sex ENUM('Male', 'Female') NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(100) UNIQUE,
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Create TABLE Teacher (
    Teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    Staff_id INT,
    Subject VARCHAR(50) NOT NULL,
    Classroom VARCHAR(20) NOT NULL,
    FOREIGN KEY Staff_id REFERENCES Staff(Staff_id)
);

CREATE TABLE Admin (
    Admin_id INT PRIMARY KEY AUTO_INCREMENT,
    Staff_id INT,
    Deepartment VARCHAR(100) NOT NULL,
    FOREIGN KEY Staff_id REFERENCES Staff(Staff_id)
)

INSERT INTO Students (Fname, Sname, Sex, Email) VALUES ('Alice', 'Smith', 'Female', 'Alice232@example.com');
INSERT INTO Students (Fname, Sname, Sex, Email) VALUES ('Leon', 'Straßmann', 'Male', 'LeonStaß@example.com');
INSERT INTO Students (Fname, Sname, Sex, Email) VALUES ('Mia', 'Straßmann', 'Female', 'MiaStaß@example.com');

INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Wilhelm', 'Straßmann', 'Male', 'StarßmannWilh@example.com');
INSERT INTO Teacher (Teacher_id, Subject, Classroom) VALUES (LAST_INSERT_ID(), 'Mathematics', 'Rm205');
INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Ursula', 'Müller', 'Female', 'UrsMueller@example.com');
INSERT INTO Teacher (Teacher_id, Subject, Classroom) VALUES (LAST_INSERT_ID(), 'German', 'Rm504');
INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Karl', 'Schneider', 'Male', 'Shneider02@example.com');
INSERT INTO Teacher (Teacher_id, Subject, Classroom) VALUES (LAST_INSERT_ID(), 'Informatics', 'CL4');

INSERT INTO Saff (Fname, Sname, Sex, Email) VALUES ('Mia', 'Schneider', 'Feale', 'Shneider02@example.com');
INSERT INTO Admin (Teacher_id, Department) VALUES (LAST_INSERT_ID(), 'Examinations');

SELECT * FROM users;