-- To run this file:
	-- mysql -uroot -pmysql
	-- source xx/note_02.sql

-- Prepare data
	-- create a database
	create database test charset=utf8;
	use test;
	-- View current database
	-- select database();

	-- create some table examples
	create table student(
		id int unsigned primary key auto_increment not null,
		name varchar(20) default '',
		age tinyint unsigned default 0,
		height decimal(5, 2),
		gender enum("Male", "Female", "Unisex", "Others"),
		cls_id int unsigned default 0,
		is_delete bit default 0
		);

	create table class(
		id int unsigned not null primary key auto_increment,
		name varchar(30) not null
	);

	-- Create some random data
	insert into student values
	(0, "Alice", 18, 167.00, 2, 1, 0),
	(0, "Bob", 19, 170.00, 1, 2, 0),
	(0, "Catlyn", 20, 169.00, 2, 1, 0),
	(0, "Danny", 19, 178.00, 1, 3, 0),
	(0, "Elvin", 22, 188.00, 1, 2, 0),
	(0, "Finn", 18, 178.00, 3, 5, 0),
	(0, "Grace", 28, 165.00, 2, 3, 0),
	(0, "Hailey", 38, 160.00, 2, 3, 0),
	(0, "Iris", 18, 169.00, 1, 1, 0),
	(0, "Jake", 20, 180.00, 1, 3, 1),
	(0, "Lorren", 23, 187.00, 1, 6, 0),
	(0, "Matty", 24, 189.00, 1, 3, 0),
	(0, "Nancy", 19, 168.00, 2, 2, 0),
	(0, "Otis", 16, 170.00, 4, 2, 0);

	insert into class values
	(0, "class_01"),
	(0, "class_02"),
	(0, "class_03"),
	(0, "class_04"),
	(0, "class_05"),
	(0, "class_06");

-- Retrieve
	-- retrieve all field
	select * from student;
	select * from class;
	-- retrieve specific field
	select name, age from student;
	select s.name, s.age from student as s;
	-- ELIMINATE DUPLICATE
	select distinct gender from student;

-- Conditional retrieve
	-- select ... from ... where ...
	-- Comparison operator
		-- greater: >
		-- smaller: <
		-- not equal: != | <>
	select * from student where age>18;

	-- Logic operator
	-- and or not
	select * from student where age>18 and age<28;
	select * from student where gender="Female" and age>18;
	select * from student where height>180 or age>18;
	select * from student where not (gender="Female" and age>18);

-- Vague retrieve
	-- like
	-- % substitute character >= 0
	-- _ substitue one character
		-- retrieve students whose name starts with A
		select name from student where name like "A%";
		-- retrieve students whose name has letter i
		select name from student where name like "%i%";
		-- retrieve students whose name has 4 letters
		select name from student where name like "____";

	-- rlike
		-- retrieve students whose name starts with A
		select name from student where name rlike "^A.*";
		-- retrieve students whose name has letter i
		select name from student where name rlike ".*i.*";
		-- retrieve students whose name has 4 letters
		select name from student where name rlike "/w{4}";

-- Range retrieve
	-- in (xxx)
	select name, age from student where age in (18, 19, 22);
	select name, age from student where age not in (18, 19, 22);

	-- between .. and ..	-> [18, 24]
	select name, age from student where age not between 18 and 24;

	select name, age from student where height is null;
	select name, age from student where height is not null;

-- Sorting
	-- order by asc/desc
	select name, age from student where height>170 and gender="Male" order by age asc, id desc;


-- Function
	-- count()
	select count(*) from student where gender=1;
	select count(*) as num_male from student where gender=1;
	-- max()
	select max(age) as max_age from student where gender=1;
