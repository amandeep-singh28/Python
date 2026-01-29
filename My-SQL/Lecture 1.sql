-- create database name; -- Create Database

-- use name; 

-- create table student (
-- 	id INT PRIMARY KEY,
--     name VARCHAR(50),
--     age INT NOT NULL
-- );

-- INSERT INTO student values(
-- 	101, "Amandeep", 21
-- ); -- It will only 1 row

-- SELECT * FROM student;

-- INSERT INTO student (id, name, age)
-- VALUES
-- (102, "Ravi", 22),
-- (103, "Raj", 19);


CREATE DATABASE college;
USE college;

CREATE TABLE student (
	RollNo INT PRIMARY KEY,
    Name VARCHAR(50),
    Marks INT Not Null,
    Grade VARCHAR(1),
    City VARCHAR(20)
);

INSERT INTO student
(RollNo, Name, Marks, Grade, City)
VALUES
(101, "Anil", 78, "C", "Pune"),
(102, "Bhumika", 93, "A", "Mumbai"),
(103, "Chetan", 85, "B", "Mumbai"),
(104, "Dhruv", 96, "A", "Delhi"),
(105, "Emanuel", 12, "F", "Delhi"),
(106, "Farah", 82, "B", "Delhi");

SELECT * FROM student;

SELECT * FROM student
WHERE (City like "Mumbai") OR (Marks > 90);

SELECT * FROM student LIMIT 3;

SELECT AVG(Marks) AS Average_Marks FROM student;

SELECT MIN(Marks) AS Min_Marks FROM student;

SELECT MAX(Marks) AS Max_Marks FROM student;

SELECT SUM(Marks) AS Total_Marks FROM student;

SELECT City, SUM(Marks) AS Total_Marks
FROM student
GROUP BY City;



