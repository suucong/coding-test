-- 코드를 입력하세요
with all_sales as (
    select shipment_id, flavor, total_order from first_half
    union all
    select shipment_id, flavor, total_order from july
),
ranked_sales as (
    select flavor,
        rank() over (order by sum(total_order) desc) as rnk
    from all_sales
    group by flavor
)
select flavor
from ranked_sales
where rnk <= 3;
