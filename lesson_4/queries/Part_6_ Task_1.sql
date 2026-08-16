-- 1 Find ProjectName
--select 
--	p.projectname
--from projects p 
--join employeeprojects e on p.projectid = e.projectid 
--join employees e2 on e.employeeid = e2.employeeid 
--where e2.firstname || ' ' || e2.lastname = 'Bob Johnson' 
--	and e.hoursworked >= 150


-- 2 There’s no one from the IT department, so Senior IT
--update projects 
--set budget = budget * 1.1 
--where exists(
--	select 1
--	from employeeprojects e2
--	join employees e on e2.employeeid = e.employeeid
--	where e2.projectid = projects.projectid
--		and e.department = 'Senior IT'
--)
--
--select *
--from projects p 

-- 3 Create new
--insert into projects (projectname, budget, startdate)
--values ('Test2', 2000, '2026-03-03')
--
--update projects 
--set enddate = startdate + INTERVAL '1 year'
--where enddate is null
--
--select *
--from projects p 


-- 4 Insert
-- It’s not working, I don’t understand where the error is.
begin;

WITH new_employee AS (
    INSERT INTO employees (firstname, lastname, department, salary, email)
    VALUES ('Dan', 'Smith', 'IT', 10000, '2@.com')
    RETURNING employeeid
)
insert into employeeprojects (employeeid, projectid, hoursworked)
select
	ne.employeeid,
	p.projectid,
	80
from new_employee ne
join employeeprojects e on ne.employeeid = e.employeeid
join projects p on e.projectid = p.projectid 
where p.projectname = 'Website Redesign'
returning employeeid, projectid, hoursworked

select *
from employees e 

commit;


