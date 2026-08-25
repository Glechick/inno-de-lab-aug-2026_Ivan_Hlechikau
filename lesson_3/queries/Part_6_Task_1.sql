-- For each order, add a column with the customer total order amount
select 
	o.order_id,
	o.customer_id,
	o.item, 
	o.amount,
	SUM(o.amount) over(
		partition by o.customer_id
	) as total_by_customer
from orders o 
order by o.order_id, o.customer_id 

