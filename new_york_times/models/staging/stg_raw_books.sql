{{ config(materialized="incremental", unique_key=["list_id", "results_id", "title"]) }}

with
    raw_books as (
        select
            list_id,
            results_id,
            age_group,
            author,
            contributor,
            contributor_note,
            description,
            price,
            primary_isbn13,
            primary_isbn10,
            publisher,
            "rank",
            title,
            created_date,
            updated_date,
            created_at
        from {{ source("raw_data", "raw_books") }}
    )

select *
from raw_books

{% if is_incremental() %}
    where created_at > (select max(created_at) from {{ this }})
{% endif %}
