use school_mgmt;

CREATE TABLE IF NOT EXISTS class(
class_id int primary key auto_increment,
course_code varchar(30),
term varchar(30),
section_num int,
class_desc varchar(100),
class_status INT DEFAULT 0
 );
 
CREATE TABLE IF NOT EXISTS student(
student_id int primary key auto_increment,
student_name text,
email varchar(100) generated always as (concat(username, '@gmail.com')) stored,
username varchar(50)
);

CREATE TABLE IF NOT EXISTS enroll(
enrollment_id int primary key auto_increment,
class_id int,
student_id int,
foreign key (class_id) references class(class_id),
foreign key (student_id) references student(student_id));


CREATE TABLE IF NOT EXISTS category(
category_id int primary key auto_increment,
category_name varchar(30),
weight FLOAT,
class_id int,
foreign key (class_id) references class(class_id));

CREATE TABLE IF NOT EXISTS assignment(
assignment_id int primary key auto_increment,
assignment_name varchar(30),
class_id int,
category_id int,
assignment_desc varchar(50),
points float,
unique key unique_assignment(class_id, category_id, assignment_name),
foreign key (class_id) references class(class_id),
foreign key (category_id) references category(category_id));

CREATE TABLE IF NOT EXISTS grade(
grade_id int primary key auto_increment,
student_id int,
assignment_id int,
grade float,
foreign key (student_id) references student(student_id),
foreign key (assignment_id) references assignment(assignment_id));

#class table
insert into class(course_code, term, section_num, class_desc) values ('CS410','Fall23',1,'Databases');
insert into class(course_code, term, section_num, class_desc) values ('CS410','Fall23',2,'Databases');

#student table
insert into student(student_name, username) values ('abc','abc');
insert into student (student_name, username) values ('Hewet Redley', 'hredley0');
insert into student (student_name, username) values ('Theobald Devenport', 'tdevenport1');
insert into student (student_name, username) values ('Robert Dran', 'rdran2');
insert into student (student_name, username) values ('Nicolas Jossel', 'njossel3');
insert into student (student_name, username) values ('Bran Cambridge', 'bcambridge4');
insert into student (student_name, username) values ('Lorrie Maciaszek', 'lmaciaszek5');
insert into student (student_name, username) values ('Stevy Mariel', 'smariel6');
insert into student (student_name, username) values ('Tammy Rubanenko', 'trubanenko7');
insert into student (student_name, username) values ('Rochell de Voiels', 'rde8');
insert into student (student_name, username) values ('Merna Cavan', 'mcavan9');
insert into student (student_name, username) values ('Aleda Laudham', 'alaudhama');
insert into student (student_name, username) values ('Halli Asser', 'hasserb');
insert into student (student_name, username) values ('Chilton Smallpeice', 'csmallpeicec');
insert into student (student_name, username) values ('Honey Grandison', 'hgrandisond');
insert into student (student_name, username) values ('Anders Bycraft', 'abycrafte');
insert into student (student_name, username) values ('Elly Tellenbrook', 'etellenbrookf');
insert into student (student_name, username) values ('Ravi Olivelli', 'rolivellig');
insert into student (student_name, username) values ('Huey Simonite', 'hsimoniteh');
insert into student (student_name, username) values ('Brittney Wreakes', 'bwreakesi');
insert into student (student_name, username) values ('Wren Linke', 'wlinkej');
insert into student (student_name, username) values ('Shalna Mayston', 'smaystonk');
insert into student (student_name, username) values ('Ennis Poley', 'epoleyl');
insert into student (student_name, username) values ('Waiter Rickhuss', 'wrickhussm');
insert into student (student_name, username) values ('Verne Grimsdell', 'vgrimsdelln');
insert into student (student_name, username) values ('Linda Cranefield', 'lcranefieldo');
insert into student (student_name, username) values ('Lane Hillhouse', 'lhillhousep');
insert into student (student_name, username) values ('Domingo Sanbrook', 'dsanbrookq');
insert into student (student_name, username) values ('Carolee Sexstone', 'csexstoner');
insert into student (student_name, username) values ('Ethelyn Leverson', 'eleversons');

#enroll table
insert into enroll (class_id, student_id) values (1, 1);
insert into enroll (class_id, student_id) values (1, 2);
insert into enroll (class_id, student_id) values (1, 3);
insert into enroll (class_id, student_id) values (1, 4);
insert into enroll (class_id, student_id) values (1, 5);
insert into enroll (class_id, student_id) values (1, 6);
insert into enroll (class_id, student_id) values (1, 7);
insert into enroll (class_id, student_id) values (1, 8);
insert into enroll (class_id, student_id) values (1, 9);
insert into enroll (class_id, student_id) values (1, 10);
insert into enroll (class_id, student_id) values (2, 11);
insert into enroll (class_id, student_id) values (2, 12);
insert into enroll (class_id, student_id) values (2, 13);
insert into enroll (class_id, student_id) values (2, 14);
insert into enroll (class_id, student_id) values (2, 15);

#category table
insert into category(category_name, weight, class_id) values('Homeworks',0.4,1);
insert into category(category_name, weight, class_id) values('Exams',0.3,1);
insert into category(category_name, weight, class_id) values('Project',0.3,1);
insert into category(category_name, weight, class_id) values('Homeworks',0.4,2);
insert into category(category_name, weight, class_id) values('Exams',0.3,2);
insert into category(category_name, weight, class_id) values('Project',0.3,2);

#assignment table
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Homework 1', 1,1,'E-R diagrams',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Homework 2', 1,1,'Normalization',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Midterm 1', 1,2,'Till E-R diagrams',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Midterm 2', 1,2,'Normalization & Transactions',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Final Exam', 1,2,'Full Syllabus',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Final Project', 1,3,'Application of DBMS',100);
select * from assignment;
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Homework 1', 2,5,'E-R diagrams',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Homework 2', 2,5,'Normalization',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Midterm 1', 2,6,'Till E-R diagrams',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Midterm 2', 2,6,'Normalization & Transactions',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Final Exam', 2,6,'Full Syllabus',100);
insert into assignment(assignment_name,class_id,category_id,assignment_desc,points) values('Final Project', 2,7,'Application of DBMS',100);

#grade table
#class_id=1 grades
insert into grade(student_id,assignment_id,grade) values(1,1,80);
insert into grade(student_id,assignment_id,grade) values(1,2,100);
insert into grade(student_id,assignment_id,grade) values(1,3,90);
insert into grade(student_id,assignment_id,grade) values(1,4,90);
insert into grade(student_id,assignment_id,grade) values(1,5);
insert into grade(student_id,assignment_id) values(1,6);
insert into grade(student_id,assignment_id,grade) values(2,1,85);
insert into grade(student_id,assignment_id,grade) values(2,2,95);
insert into grade(student_id,assignment_id,grade) values(2,3,80);
insert into grade(student_id,assignment_id,grade) values(2,4,75);
insert into grade(student_id,assignment_id,grade) values(2,5,80);
insert into grade(student_id,assignment_id,grade) values(2,6,85);

insert into grade(student_id,assignment_id,grade) values(3,1,75);
insert into grade(student_id,assignment_id,grade) values(3,2,85);
insert into grade(student_id,assignment_id,grade) values(3,3,80);
insert into grade(student_id,assignment_id,grade) values(3,4,95);
insert into grade(student_id,assignment_id,grade) values(3,5,82);
insert into grade(student_id,assignment_id,grade) values(3,6,90);

insert into grade(student_id,assignment_id,grade) values(4,1,71);
insert into grade(student_id,assignment_id,grade) values(4,2,83);
insert into grade(student_id,assignment_id,grade) values(4,3,90);
insert into grade(student_id,assignment_id,grade) values(4,4,85);
insert into grade(student_id,assignment_id,grade) values(4,5,82);
insert into grade(student_id,assignment_id,grade) values(4,6,70);

insert into grade(student_id,assignment_id,grade) values(33,1,94);
insert into grade(student_id,assignment_id,grade) values(33,2,84);
insert into grade(student_id,assignment_id,grade) values(33,3,91);
insert into grade(student_id,assignment_id,grade) values(33,4,95);
insert into grade(student_id,assignment_id,grade) values(33,5,85);
insert into grade(student_id,assignment_id,grade) values(33,6,90);

insert into grade(student_id,assignment_id,grade) values(35,1,81);
insert into grade(student_id,assignment_id,grade) values(35,2,83);
insert into grade(student_id,assignment_id,grade) values(35,3,91);
insert into grade(student_id,assignment_id,grade) values(35,4,75);
insert into grade(student_id,assignment_id,grade) values(35,5,86);
insert into grade(student_id,assignment_id,grade) values(35,6,90);

# class_id=2 grades
insert into grade(student_id,assignment_id,grade) values(11,8,94);
insert into grade(student_id,assignment_id,grade) values(11,9,84);
insert into grade(student_id,assignment_id,grade) values(11,10,91);
insert into grade(student_id,assignment_id,grade) values(11,11,95);
insert into grade(student_id,assignment_id,grade) values(11,12,85);
insert into grade(student_id,assignment_id,grade) values(11,13,90);

insert into grade(student_id,assignment_id,grade) values(13,8,75);
insert into grade(student_id,assignment_id,grade) values(13,9,85);
insert into grade(student_id,assignment_id,grade) values(13,10,80);
insert into grade(student_id,assignment_id,grade) values(13,11,95);
insert into grade(student_id,assignment_id,grade) values(13,12,82);
insert into grade(student_id,assignment_id,grade) values(13,13,90);