with
    filtered_rankings as (
        select f.book_id, b.title, f.bestsellers_date
        from {{ ref("fact_books_rankings") }} f
        join {{ ref("dim_books") }} b on f.book_id = b.book_id
        where f.rank <= 3 and f.bestsellers_date between '2022-01-01' and '2022-12-31'
    ),
    book_counts_days as (
        select title, count(*) as total_days_in_top_3
        from filtered_rankings
        group by title
    )

select *
from book_counts_days
order by total_days_in_top_3 desc
limit 1

