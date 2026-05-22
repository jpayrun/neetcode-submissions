-- Write your query below

select
    customer_id
from customers
where
    year = 2020
group by 
    1
having 
    sum(revenue) > 0
