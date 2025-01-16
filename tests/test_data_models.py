
from src.ingestion.data_models import RawResults


def test_raw_results():
    raw_results = RawResults(
        results_id="id",
        status="ok",
        copyright="rights reserved",
        num_results=200,
        bestsellers_date="2015-03-04",
        published_date="2015-03-04",
        published_date_description="2015-03-04",
        previous_published_date="2015-03-04",
        next_published_date="2015-03-04",
        created_at=1737054707.6667964,
    )

    actual_results = raw_results.dict()

    assert actual_results == {
        "results_id": "id",
        "status": "ok",
        "copyright": "rights reserved",
        "num_results": 200,
        "bestsellers_date": "2015-03-04",
        "published_date": "2015-03-04",
        "published_date_description": "2015-03-04",
        "previous_published_date": "2015-03-04",
        "next_published_date": "2015-03-04",
        "created_at": 1737054707.6667964,
    }
