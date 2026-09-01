-- a list of orders together with the status and name of the castomer
select 
	c.country,
	count(c.customer_id) count
from customers c
group by c.country