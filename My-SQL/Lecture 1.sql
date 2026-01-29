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



CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    age         INT,
    country     VARCHAR(50)
);

INSERT INTO Customers (customer_id, first_name, last_name, age, country) VALUES
(1, 'John',   'Doe',       31, 'USA'),
(2, 'Robert', 'Luna',      22, 'USA'),
(3, 'David',  'Robinson',  22, 'UK'),
(4, 'John',   'Reinhardt', 25, 'UK'),
(5, 'Betty',  'Doe',       28, 'UAE');


CREATE TABLE Orders (
    order_id    INT PRIMARY KEY,
    item        VARCHAR(50),
    amount      INT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);


INSERT INTO Orders (order_id, item, amount, customer_id) VALUES
(1, 'Keyboard',  400,   4),
(2, 'Mouse',     300,   4),
(3, 'Monitor',   12000, 3),
(4, 'Keyboard',  400,   1),
(5, 'Mousepad',  250,   2);

CREATE TABLE Shippings (
    shipping_id INT PRIMARY KEY,
    status      VARCHAR(20),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Shippings (shipping_id, status, customer_id) VALUES
(1, 'Pending',   2),
(2, 'Pending',   4),
(3, 'Delivered', 3),
(4, 'Pending',   5),
(5, 'Delivered', 1);



SELECT C.first_name, O.item, O.item
FROM Customers C
INNER JOIN Orders O
ON C.customer_id = O.customer_id;

SELECT C.first_name
FROM Customers C
INNER JOIN Orders O
on C.customer_id = O.customer_id;

SELECT c.first_name, c.last_name, count(o.order_id) AS Number_Of_Orders
FROM Customers c
INNER JOIN Orders o
on c.customer_id = o.customer_id
GROUP BY c.customer_id;

SELECT 
    c.first_name,
    c.last_name,
    SUM(o.amount) AS total_amount
FROM Customers c
INNER JOIN Orders o
    ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id,
    c.first_name,
    c.last_name
HAVING SUM(o.amount) > 500;


-- FIND CUSTOMERS WHO ORDERD ITEMS NOT ORDERED BY ANY USA CUSTOMER

SELECT c.customer_id from Customers C WHERE Country not like "%USA%";


-- FIND CUSTOMERS WHO ORDERED THE SAME ITEM AS JOHN REINHARDT
SELECT c.customer_id FROM CUSTOMERS;


-- Customer, order item, and shipping status
SELECT c.first_name, o.item, s.status
FROM Customers c
JOIN Orders o     ON c.customer_id = o.customer_id
JOIN Shippings s  ON c.customer_id = s.customer_id;








