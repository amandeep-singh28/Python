CREATE DATABASE new_db;

USE new_db;

CREATE TABLE students(
            student_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(30),
            email VARCHAR(30) UNIQUE,
            phone INT,
            city VARCHAR(20)
);

CREATE TABLE applications(
            application_id INT PRIMARY KEY,
            student_id INT,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            course VARCHAR(20),
            marks INT,
            status VARCHAR(30),
            applied_date DATE
);

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE applications;
TRUNCATE TABLE students;

SET FOREIGN_KEY_CHECKS = 1;



