with
    unique_books_per_list as (
        select f.list_id, l.display_name, count(distinct f.book_id) as unique_books
        from {{ ref("fact_books_rankings") }} f
        join {{ ref("dim_lists") }} l on f.list_id = l.list_id
        group by f.list_id, l.display_name
    )

select *
from unique_books_per_list
order by unique_books asc
limit 3

