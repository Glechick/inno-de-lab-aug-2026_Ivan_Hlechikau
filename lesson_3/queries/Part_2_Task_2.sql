-- a list of orders together with the status and name of the customer
select 
	s.status,
	c.first_name,
	c.last_name
from shippinings s
join customers c on s.customer = c.customer_id