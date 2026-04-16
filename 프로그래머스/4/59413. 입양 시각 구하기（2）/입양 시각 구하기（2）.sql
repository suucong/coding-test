-- 코드를 입력하세요
with 
recursive hours as (
    select 0 as hour        
    union all
    select hour + 1 from hours 
    where hour < 23         
),
count_animal_outs as (
    select hour(datetime) as hour, count(*) as cnt
    from animal_outs
    group by hour(datetime)
)
select h.hour, coalesce(a.cnt, 0)
from hours h
    left join count_animal_outs a on h.hour = a.hour;