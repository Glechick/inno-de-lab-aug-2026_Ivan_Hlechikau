-- Tnsert
--insert into Employees (FirstName, LastName, Department, Salary)
--values
--	('Dan', 'Jonson', 'HR', '55000'),
--	('Diana', 'Brown', 'Finance', '60000')

-- Select
--select *
--from Employees

-- Select with condition
--select 
--	e.firstname, 
--	e.lastname 
--from employees e 
--where e.department = 'IT'

update employees
set salary = '65000'
where firstname = 'Alise' and  lastname = 'Smith'

select *
from Employees