-- a list of orders together with the name of the customer who placed the order
select 
	o.order_id,
	o.item,
	o.amount,
	o.customer_id
from orders o
where o.amount > 1000