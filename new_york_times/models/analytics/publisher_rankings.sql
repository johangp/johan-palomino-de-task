with
    publisher_points as (
        select
            d.publisher,
            date_trunc('quarter', f.bestsellers_date) as quarter,
            sum(
                case
                    when f.rank = 1
                    then 5
                    when f.rank = 2
                    then 4
                    when f.rank = 3
                    then 3
                    when f.rank = 4
                    then 2
                    when f.rank = 5
                    then 1
                    else 0
                end
            ) as total_points
        from {{ ref("fact_books_rankings") }} f
        join {{ ref("dim_books") }} d on f.book_id = d.book_id
        where f.bestsellers_date between '2021-01-01' and '2023-12-31'
        group by d.publisher, quarter
    ),
    ranked_publishers as (
        select
            publisher,
            quarter,
            total_points,
            rank() over (partition by quarter order by total_points desc) as rank
        from publisher_points
    )

select *
from ranked_publishers
where rank <= 5
order by quarter, rank

