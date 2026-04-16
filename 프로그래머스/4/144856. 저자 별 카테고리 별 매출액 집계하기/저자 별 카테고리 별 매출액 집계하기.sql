-- 코드를 입력하세요
select c.author_id, max(author_name) as author_name, 
    b.category, sum(b.price * a.sales) total_sales
from book_sales a
    join book b on a.book_id = b.book_id
    join author c on b.author_id = c.author_id
where date_format(a.sales_date, '%Y-%m') = '2022-01'
group by c.author_id, b.category
order by author_id asc, category desc;