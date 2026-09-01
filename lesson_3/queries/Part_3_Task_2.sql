-- the total number of orders and the avarage amount for each product
select 
	c.country, 
	count(c.customer_id) count
from customers c
group by c.country 