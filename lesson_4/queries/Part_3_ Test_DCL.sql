-- Select correct
--SELECT *
--FROM employees

-- Insert
--insert into employees (firstname, lastname, department, salary, email) 
--values ('Anna', 'Annovna', 'IT', 67000, 'a@.com');

-- Insert and Update
insert into employees (firstname, lastname, department, salary, email) 
values ('Anna', 'Annovna', 'IT', 67000, 'a@.com');

update employees 
set employeeid = 67
where salary = 67000

SELECT *
FROM employees

