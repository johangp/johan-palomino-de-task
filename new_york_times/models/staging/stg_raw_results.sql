with
    raw_results as (
        select
            results_id,
            status,
            copyright,
            num_results,
            bestsellers_date,
            published_date,
            created_at
        from {{ source("raw_data", "raw_results") }}
    )

select *
from raw_results

