-- All orders with an amount more then 1000
select 
	o.orderid,
	o.item,
	o.amount,
	o.customer
from orders o
where o.amount > 1000
