-- a list of orders together with the name of the customer who placed the order
select 
	c.first_name,
	c.last_name,
	o.item,
	o.amount
from orders o
join customer c on o.customer_id = c.customer_id