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
            created_at,
            row_number() over (
                partition by title, primary_isbn13
                order by updated_date desc, created_at desc
            ) as row_num
        from {{ source("raw_data", "raw_books") }}
    )

select *
from raw_books
where row_num = 1

