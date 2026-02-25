create database assessment
use assessment
CREATE TABLE student( 
    student_id INT AUTO_INCREMENT PRIMARY KEY, 
    stud_name varchar(50) NOT null, 
    country varchar(50) NOT null, 
    registration_Date date 
   ); 
   CREATE table course( 
    course_id int AUTO_INCREMENT PRIMARY KEY, 
    title varchar(50) NOT null, 
    subject varchar(50) NOT null, 
    level varchar(50) NOT null); 
    
    CREATE TABLE enrollment( 
    enroll_Date date, 
    stud_id INT NOT null, 
    c_id INT NOT null, 
    FOREIGN KEY(stud_id) REFERENCES student(student_id), 
    FOREIGN KEY(c_id) REFERENCES course(course_id) 
    ); 
    
    CREATE TABLE progress( 
    stud_id INT NOT null, 
    c_id INT NOT null, 
FOREIGN KEY(stud_id) REFERENCES student(student_id), 
FOREIGN KEY(c_id) REFERENCES course(course_id), 
completed_percent decimal(5,2) NOT null, 
last_accessed date); 

INSERT INTO student (student_id, stud_name, country, registration_date) VALUES
(1, 'Aarav Sharma', 'India', '2025-01-10'),
(2, 'Emily Johnson', 'USA', '2025-02-15'),
(3, 'Rohan Mehta', 'India', '2025-03-05'),
(4, 'Sophia Brown', 'UK', '2025-01-25'),
(5, 'Daniel Lee', 'Canada', '2025-04-12'),
(6, 'Dixita Khimami', 'India', '2025-07-07'),
(7, 'Nidhi Patel', 'USA', '2025-08-28'),
(8, 'Harsh Jain', 'Canada', '2025-04-20');


INSERT INTO course (course_id, title, subject, level) VALUES
(101, 'SQL', 'Joins','Intermediate'),
(102, 'SQL', 'Normalization','Beginner'),
(103, 'SQL', 'Crud','Advanced'),
(104, 'Python', 'Functions', 'Advanced'),
(105, 'Python', 'OOPS', 'Intermediate'),
(106, 'Data Analytics', 'Excel', 'Beginner'),
(107, 'Data Analytics Basics', 'PowerBI', 'Advanced'),
(108, 'Machine Learning', 'AI', 'Intermediate');
select * from course


INSERT INTO enrollment (enroll_date, stud_id, c_id) VALUES
('2025-01-15', 1, 101),
('2025-02-01', 1, 104),
('2025-02-20', 2, 102),
('2025-03-10', 2, 106),
('2025-03-12', 3, 103),
('2025-04-01', 3, 105),
('2025-01-30', 4, 101),
('2025-02-18', 4, 107),
('2025-04-20', 5, 108),
('2025-07-10', 6, 105),
('2025-07-15', 6, 107),
('2025-09-01', 7, 102),
('2025-04-25', 8, 106),
('2025-05-02', 8, 103);

INSERT INTO progress (stud_id, c_id, completed_percent, last_accessed) VALUES
(1, 101, 80.00, '2025-02-10'),
(1, 104, 45.50, '2025-02-20'),
(2, 102, 100.00, '2025-03-05'),
(2, 106, 60.25, '2025-03-25'),
(3, 103, 70.75, '2025-04-10'),
(3, 105, 40.00, '2025-04-15'),
(4, 101, 90.00, '2025-02-28'),
(4, 107, 50.50, '2025-03-10'),
(5, 108, 30.00, '2025-05-01'),
(6, 105, 85.25, '2025-07-20'),
(6, 107, 20.00, '2025-07-25'),
(7, 102, 55.00, '2025-09-10'),
(8, 106, 95.00, '2025-05-15'),
(8, 103, 65.80, '2025-05-20');

--  Find the most popular course per subject (by enrollments).  
SELECT course.subject,
       enrollment.enroll_date,
       COUNT(enrollment.stud_id) AS most_popular
FROM enrollment  
INNER JOIN course 
    ON enrollment.c_id = course.course_id  
GROUP BY course.subject, enrollment.enroll_date
ORDER BY most_popular DESC;

--  List students who completed more than 80% in at least 3 courses. 
SELECT student.stud_name,COUNT(progress.c_id) AS more_than_3 
FROM progress 
INNER JOIN student ON progress.stud_id=student.student_id 
INNER JOIN course ON progress.c_id=course.course_id 
WHERE progress.completed_percent>80 
GROUP BY student.stud_name 
HAVING  more_than_3>=3; 

-- Calculate average course completion by level (e.g., beginner, intermediate). 
SELECT AVG(progress.completed_percent) AS avg_percentage, course.level 
FROM progress 
INNER JOIN course ON course.course_id=progress.c_id 
GROUP BY course.level;  

-- . Identify students inactive for more than 60 days.  
SELECT student.student_id, student.stud_name, student.country, progress.last_accessed 
FROM student 
LEFT JOIN progress ON progress.stud_id = student.student_id 
WHERE progress.last_accessed < DATE_SUB(CURDATE(), INTERVAL 60 DAY) 
OR progress.last_accessed IS NULL; 

--  Determine the subject with the highest average completion rate.
SELECT course.subject,AVG(progress.completed_percent)AS avg_completion_rate 
FROM progress 
INNER JOIN course ON progress.c_id=course.course_id 
GROUP BY course.subject 
ORDER BY avg_completion_rate DESC; 


