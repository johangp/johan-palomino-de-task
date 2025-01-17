{{ config(materialized="incremental", unique_key="results_id") }}

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

{% if is_incremental() %} where created_at > (select max(created_at) from {{ this }}) {% endif %}

