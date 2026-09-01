/* 
Find customers who:
    1. Have placed at least 2 orders (any),
    2. Have at least one delivery with the status 'Delivered'.
For each such customer, output:
	* full_name (first name + last name),
	* total number of orders,
	* total order amount,
	* country of residence.
*/
with order_stats as (
	select 
		c.first_name ||' '|| c.last_name full_name, 
		c.country, 
		count(o.order_id) as total_orders,
		SUM(o.amount) as total_amount
	from customers c 
	cross join orders o on c.customer_id  = o.customer_id 
	cross join shippings s on c.customer_id = s.customer 
	group by c.first_name, c.last_name, c.country
	having count(distinct o.order_id) >= 2
		and count(case when s.status = 'Delivered' then 1 end) >= 1
)
select 
	os.full_name,
	os.country,
	os.total_orders,
	os.total_amount
from order_stats os



