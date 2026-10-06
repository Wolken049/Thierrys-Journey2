USE School;

SHOW tables;
INSERT INTO Students(Fname, Sname, Sex, Email) VALUES 
('Karl', 'Schmidt', 'Male', 'KarlS@example.com');

INSERT INTO Staff(Fname, Sname, Sex, Email)
VALUES ('Marie', 'Schmidt', 'Female', 'SchmidtMarie@example.com');
INSERT INTO Teacher(Staff_id, Subject, Classroom)
VALUES (LAST_INSERT_ID(), Informatics, 'CL1');

SELECT * 
FROM Students
WHERE Fname = 'Marie'