{{ config(materialized="incremental", unique_key=["list_id", "results_id"]) }}

with
    raw_lists as (
        select
            list_id,
            results_id,
            list_name,
            display_name,
            updated,
            list_image,
            created_at
        from {{ source("raw_data", "raw_lists") }}
    )

select *
from raw_lists

{% if is_incremental() %}
    where created_at > (select max(created_at) from {{ this }})
{% endif %}

