from src.ingestion.data_models import RawBook, RawList, RawResults


def test_raw_results():
    raw_results = RawResults(
        results_id="id",
        status="ok",
        copyright="rights reserved",
        num_results=200,
        bestsellers_date="2015-03-04",
        published_date="2015-03-04",
        created_at="2025-01-16 21:16:31",
    )

    actual_results = raw_results.dict()

    assert actual_results == {
        "results_id": "id",
        "status": "ok",
        "copyright": "rights reserved",
        "num_results": 200,
        "bestsellers_date": "2015-03-04",
        "published_date": "2015-03-04",
        "created_at": "2025-01-16 21:16:31",
    }


def test_raw_list():
    raw_list = RawList(
        list_id=1,
        results_id="id",
        list_name="fiction",
        display_name="combined",
        updated="weekly",
        list_image="url",
        created_at="2025-01-16 21:16:31",
    )

    actual_list = raw_list.dict()

    assert actual_list == {
        "list_id": 1,
        "results_id": "id",
        "list_name": "fiction",
        "display_name": "combined",
        "updated": "weekly",
        "list_image": "url",
        "created_at": "2025-01-16 21:16:31",
    }


def test_raw_book():
    raw_book = RawBook(
        list_id=1,
        results_id="id",
        age_group="",
        author="Clive Cussler and Justin Scott",
        contributor="by Clive Cussler and Justin Scott",
        contributor_note="a note",
        description="In the ninth book",
        price=0,
        primary_isbn13="9780698406421",
        primary_isbn10="698406427",
        publisher="Putnam",
        rank=1,
        title="THE GANGSTER",
        created_date="2016-03-10 17:00:21",
        updated_date="2016-03-10 17:00:21",
        created_at="2025-01-16 21:16:31",
    )

    actual_book = raw_book.dict()

    assert actual_book == {
        "list_id": 1,
        "results_id": "id",
        "age_group": "",
        "author": "Clive Cussler and Justin Scott",
        "contributor": "by Clive Cussler and Justin Scott",
        "contributor_note": "a note",
        "description": "In the ninth book",
        "price": 0,
        "primary_isbn13": "9780698406421",
        "primary_isbn10": "698406427",
        "publisher": "Putnam",
        "rank": 1,
        "title": "THE GANGSTER",
        "created_date": "2016-03-10 17:00:21",
        "updated_date": "2016-03-10 17:00:21",
        "created_at": "2025-01-16 21:16:31",
    }
