CREATE DATABASE School;
USE School;

CREATE TABLE Students (
    Student_id INT PRIMARY KEY AUTO_INCREMENT,
    Fname VARCHAR(100) NOT NULL,
    Sname VARCHAR(100) NOT NULL,
    Sex ENUM('Male', 'Female') NOT NULL,
    Email VARCHAR(100) UNIQUE
);

CREATE TABLE Staff (
    Staff_id INT PRIMARY KEY AUTO_INCREMENT,
    Fname VARCHAR(100) NOT NULL,
    Sname VARCHAR(100) NOT NULL,
    Sex ENUM('Male', 'Female') NOT NULL,
    Email VARCHAR(100) UNIQUE
);


CREATE TABLE Teacher (
    Teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    Staff_id INT,
    Subject VARCHAR(50) NOT NULL,
    Classroom VARCHAR(20) NOT NULL,
    FOREIGN KEY (Staff_id) REFERENCES Staff(Staff_id)
);

CREATE TABLE Admin (
    Admin_id INT PRIMARY KEY AUTO_INCREMENT,
    Staff_id INT,
    Department VARCHAR(100) NOT NULL, -- Fixed Spelling
    FOREIGN KEY (Staff_id) REFERENCES Staff(Staff_id)
);

INSERT INTO Students (Fname, Sname, Sex, Email) VALUES 
('Alice', 'Smith', 'Female', 'alice232@example.com'),
('Leon', 'Straßmann', 'Male', 'leon@example.com'),
('Mia', 'Straßmann', 'Female', 'mia_s@example.com');



INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Wilhelm', 'Straßmann', 'Male', 'wilhelm@example.com');
INSERT INTO Teacher (Staff_id, Subject, Classroom) VALUES (LAST_INSERT_ID(), 'Mathematics', 'Rm205');


INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Ursula', 'Müller', 'Female', 'ursula@example.com');
INSERT INTO Teacher (Staff_id, Subject, Classroom) VALUES (LAST_INSERT_ID(), 'German', 'Rm504');


INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Karl', 'Schneider', 'Male', 'karl@example.com');
INSERT INTO Teacher (Staff_id, Subject, Classroom) VALUES (LAST_INSERT_ID(), 'Informatics', 'CL4');


INSERT INTO Staff (Fname, Sname, Sex, Email) VALUES ('Mia', 'Schneider', 'Female', 'mia_admin@example.com');
INSERT INTO Admin (Staff_id, Department) VALUES (LAST_INSERT_ID(), 'Examinations');