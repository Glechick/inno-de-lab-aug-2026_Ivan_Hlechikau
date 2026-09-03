-- Update 1
--update employees e 
--set salary = salary * 1.1 
--where e.department = 'HR'

-- Update 2
--update employees e 
--set department = 'Senior IT'
--where salary >= 70000

-- Delete
--delete from employees e
--where not exists(
--	select 1
--	from employeeprojects ep 
--	where ep.employeeid = e.employeeid 
--)

-- Transaction
start transaction;

insert into projects (projectname, budget, startdate,enddate)
values ('Test', 10, '2026-05-10', '2026-06-10')

insert into employeeprojects (employeeID, projectid,hoursworked)
values 
	(1, (select p.projectid from projects p where p.projectname = 'Test'), 80), 
	(2, (select p.projectid from projects p where p.projectname = 'Test'), 90)

select *
from employeeprojects e  	
	
commit;


select *
from employeeprojects e  