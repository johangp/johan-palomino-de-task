with
    deduplicated as (
        select distinct list_id, list_name, display_name, updated, list_image
        from {{ ref("stg_raw_lists") }}
    )

select *
from deduplicated

