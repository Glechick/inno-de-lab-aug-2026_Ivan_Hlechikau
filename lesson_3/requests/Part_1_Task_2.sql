-- All clients from "USA" and age more then 25 years
select 
	c.first_name,
	c.last_name, 
	c.age, 
	c.country 
from customers c 
where c.age > 25 and c.country in ('USA')
