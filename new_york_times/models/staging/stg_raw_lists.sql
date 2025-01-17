with
    raw_lists as (
        select
            list_id,
            results_id,
            list_name,
            display_name,
            updated,
            list_image,
            created_at,
            row_number() over (partition by list_id order by created_at desc) as row_num
        from {{ source("raw_data", "raw_lists") }}
    )

select *
from raw_lists
where row_num = 1

