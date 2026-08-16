-- Function
--create or replace function CalculateAnnualBonus (
--	employee_id Integer, salary Decimal
--)
--returns decimal
--language PLpgSQL
--as $$
--Begin
--	return salary * 0.1;
--End
--$$

-- Use Function
--select * ,
--	CalculateAnnualBonus(e.employeeid, e.salary) as bonus
--from employees e 

create or replace view IT_Department_View as
	select *
	from emloyees
	where department = 'IT'
