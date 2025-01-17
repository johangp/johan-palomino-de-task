with
    rankings as (
        select
            row_number() over () as ranking_id,
            {{ dbt_utils.generate_surrogate_key(["title", "primary_isbn13"]) }} as book_id,
            l.list_id,
            r.results_id,
            b.rank,
            r.bestsellers_date,
            r.published_date
        from {{ ref("stg_raw_books") }} b
        join {{ ref("stg_raw_lists") }} l on b.list_id = l.list_id
        join {{ ref("stg_raw_results") }} r on b.results_id = r.results_id
    )

select *
from rankings

