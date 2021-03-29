-- MySQL 
	
	-- connect to db
	mysql -uroot -p
	mysql -uroot -pmysql

	-- exit database
	exit/quit/ctrl+d

	-- sql sentance ends with ;
	-- show database version
	select version();

	-- show time
	select now();

	-- show all database
	show databases;

	-- Create database
	create database name;
	create database name charset=utf8;

	-- View created database
	show create database name;

	-- Delete database
	drop database `name-1`;
	drop database name;

	-- View current using database
	select database();

	-- Use database
	use name;

-- Database
	-- View all tables
	show tables;

	-- Create tables
	-- auto_increment: 
	-- not null:
	-- primary key:
	-- default:
	create table name_table(id int, name varchar(30));
	create table student(
		id int unsigned primary key not null auto_increment, 
		name varchar(30),
		age tinyint unsigned default 0,
		height decimal(5, 2),
		gender enum("Male", "Femal", "Others"),
		cls_id int unsigned
	);

	-- View table structure
	desc name;
	show create table name;

	-- delete table
	drop table name;

-- Table operation


	-- add field
	alter table name add name_field int;

	-- modify field: cannot rename field
	alter table name modify name_field date;

	-- change field: change name
	alter table name change name_field name_new date;

	-- delete field
	alter table name drop name_field;

-- CURD--> Create Update Retrieve Delete
	-- Create
	-- insert ALL matched data
	-- enum: could be represented by 1 2 3 4...
	insert into name values(data1, data2); -- data could be 0 null or default

	-- Partially insert
	insert into name (attr1, attr2) values(data1, data2);
	insert into name (attr1, attr2) values(data1, data2), (data3, data4);


	-- Update
	update name set attr1=data1; -- update all
	update name set attr1=data1 where id=0;
	update name set attr1=data1, attr2=data2 where id=0;


	-- Retrieve
	select * from name_table;
	select * from name_table where attr1=data1;
	select field1 as name1, field2 as name2 from name_table;

	-- Delete
	-- delete all table PHYSICALLY
	delete from name_table;
	-- delete conditionally
	delete from name_table where attr1=data1;

	-- delete LOGICALLY
	alter table name_table add is_delete bit default 0;

