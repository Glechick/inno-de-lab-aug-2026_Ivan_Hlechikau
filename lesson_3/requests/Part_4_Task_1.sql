-- the total number of orders and the avarage amount for each product
select 
	c.first_name,
	c.age 
from customers c  
group by c.first_name
order by c.age desc 

