with
    deduplicated as (
        select distinct
            {{ dbt_utils.generate_surrogate_key(["title", "primary_isbn13"]) }} as book_id,
            title,
            author,
            contributor,
            contributor_note,
            description,
            primary_isbn13,
            primary_isbn10,
            publisher,
            age_group,
            price
        from {{ ref("stg_raw_books") }}
    )

select *
from deduplicated

