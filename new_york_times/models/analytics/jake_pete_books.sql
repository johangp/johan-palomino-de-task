with
    jake_books as (
        select f.book_id, b.title, 'Jake' as team
        from {{ ref("fact_books_rankings") }} f
        join {{ ref("dim_books") }} b on f.book_id = b.book_id
        where f.rank = 1 and f.bestsellers_date between '2023-01-01' and '2023-12-31'
    ),
    pete_books as (
        select f.book_id, b.title, 'Pete' as team
        from {{ ref("fact_books_rankings") }} f
        join {{ ref("dim_books") }} b on f.book_id = b.book_id
        where f.rank = 3 and f.bestsellers_date between '2023-01-01' and '2023-12-31'
    )

select distinct
    coalesce(j.title, p.title) as book_title, coalesce(j.team, p.team) as team
from jake_books j
full outer join pete_books p on j.book_id = p.book_id

