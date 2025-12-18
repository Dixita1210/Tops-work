use dk 
create table Company (CompanyID int primary key , CompanyName varchar(45),
Street varchar (45), City varchar (45), State varchar (2), Zip varchar(10))

create table Contact ( ContactID int primary key, CompanyID int , FirstName varchar(45),
LastName varchar (45), Street varchar (45),  City varchar (45), State varchar (2), Zip varchar (10),
IsMain boolean , Email varchar (45), Phone varchar (12), foreign key (CompanyID) references Company (CompanyID))

create table ContactEmployee ( ContactEmployeeID int , ContactID int, EmployeeID int, ContactDate date, 
Description varchar (100) , foreign key (ContactID) references Contact (ContactID), foreign key (EmployeeID) 
references Employee (EmployeeID))

create table Employee ( EmployeeID int primary key, FirstName varchar (45), LastName varchar (45),
Salary decimal(10,2), HireDate date, JobTitle varchar (25), Email varchar (45) , Phone varchar(12))

INSERT INTO Company (CompanyID, CompanyName, Street, City, State, Zip) VALUES
(1, 'TechVision Inc', '12 Silicon Street', 'San Jose', 'CA', '95110'),
(2, 'HealthPlus Corp', '88 Wellness Ave', 'Austin', 'TX', '73301'),
(3, 'GreenEnergy LLC', '45 Solar Road', 'Denver', 'CO', '80202');

INSERT INTO Employee (EmployeeID, FirstName, LastName, Salary, HireDate, JobTitle, Email, Phone) VALUES
(101, 'John', 'Miller', 85000.00, '2020-03-15', 'Manager', 'john.m@tech.com', '4085551122'),
(102, 'Sara', 'Lopez', 65000.00, '2021-07-20', 'Analyst', 'sara.l@tech.com', '4085552371'),
(103, 'David', 'Patel', 72000.00, '2019-11-10', 'Sales Lead', 'david.p@health.com', '5125557862'),
(104, 'Emily', 'Stone', 54000.00, '2022-01-05', 'Coordinator', 'emily.s@green.com', '3035559921');

INSERT INTO Contact (ContactID, CompanyID, FirstName, LastName, Street, City, State, Zip,
IsMain, Email, Phone) VALUES
(201, 1, 'Michael', 'Adams', '500 Tech Park', 'San Jose', 'CA', '95111', TRUE, 'm.adams@techvision.com', '4081112222'),
(202, 1, 'Priya', 'Sharma', '700 King Lane', 'San Jose', 'CA', '95112', FALSE, 'priya.s@techvision.com', '4082223333'),
(203, 2, 'Robert', 'Smith', '90 Health St', 'Austin', 'TX', '73302', TRUE, 'robert.s@healthplus.com', '5124445555'),
(204, 3, 'Anna', 'Joseph', '15 Green Blvd', 'Denver', 'CO', '80203', TRUE, 'anna.j@greenenergy.com', '3036667777');


INSERT INTO ContactEmployee (ContactEmployeeID, ContactID, EmployeeID, ContactDate, Description) VALUES
(301, 201, 101, '2024-02-10', 'Initial business discussion'),
(302, 202, 102, '2024-02-15', 'Follow-up email sent'),
(303, 203, 103, '2024-03-01', 'Requested product demo'),
(304, 204, 104, '2024-03-05', 'Scheduled meeting with manager');

-------------------------- 4------------------------------------------------------
update Employee set Phone = '215-555-8800' where EmployeeID = 102;

-------------------------- 5------------------------------------------------------
update Company set CompanyName = 'Urban Outfitters' where CompanyID = 1;

-------------------------- 6------------------------------------------------------
delete from ContactEmployee where ContactID= ( select ContactID from Contact where FirstName= 'Priya'
and LastName= 'Sharma' ) and EmployeeID =( select EmployeeID from Employee where FirstName=' John' and 
LastName='Miller');

-------------------------- 7------------------------------------------------------
select e.FirstName,e.Lastname from Employee e join ContactEmployee ce on e.EmployeeID=ce.EmployeeID
join Contact c on ce.ContactID=c.ContactID join Company co on c.CompanyID=co.CompanyID where 
co.CompanyName='HealthPlus Corp'

-------------------------- 8------------------------------------------------------
select FirstName from Employee where FirstName like 'E%'
select * from Employee where FirstName like '_____'

-------------------------- 9 ---------------------------------------------------------
-- Normalization is a process of organizing data in a
 -- relational database to reduce duplication and improve data integrity.
 -- It organizes data into multiple related tables using primary and foreign keys.
-- Its main goal is to prevent update, insert, and delete anomalies.

----------------------------------- 10 ---------------------------------------------------
-- A JOIN in MySQL is used to combine rows from two or more
-- tables based on a related column between them.
-- JOINS work using matching keys, usually a primary key in one table and a foreign key in another.

----------------------------------- 11 -------------------------------------------------------
-- DDL (Data Definition Language)
-- Used to define or modify the structure of database objects (tables, indexes, schemas).
-- CREATE, ALTER, DROP

-- DML (Data Manipulation Language)
--  to manage and manipulate the data stored in tables.
-- INSERT, UPDATE, DELETE, SELECT.

-- (Data Control Language)
-- Used to control access and permissions on database objects.
-- GRANT, REVOKE.

-------------------------------- 12 ----------------------------------------------
-- INNER JOIN – Only matching rows from both tables.
-- LEFT JOIN – All rows from left table + matches from right.
-- RIGHT JOIN – All rows from right table + matches from left.
-- FULL OUTER JOIN – All rows from both tables, NULLs if no match.






