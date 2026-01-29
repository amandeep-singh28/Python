create database name; -- Create Database

use name; 

create table student (
	id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT NOT NULL
);

INSERT INTO student values(
	101, "Amandeep", 21
); -- It will only 1 row

SELECT * FROM student;

INSERT INTO student (id, name, age)
VALUES
(102, "Ravi", 22),
(103, "Raj", 19);





