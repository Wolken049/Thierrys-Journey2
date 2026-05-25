CREATE DATABASE Python_School;
USE Python_School;

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
