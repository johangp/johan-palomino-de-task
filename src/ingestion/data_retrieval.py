import time
from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

import requests

from .data_ingestion import DataIngestion
from .data_models import RawBook, RawList, RawResults
from .exceptions import InvalidApiKey

LISTS_OVERVIEW_ENDPOINT = "https://api.nytimes.com/svc/books/v3/lists/overview.json"
API_KEY = "H4K4FyQYZKhhlTwLitBhDG5zDjtC2Cib"  # Harcoded for the sake of simplicity
DATE_FORMAT = "%Y-%m-%d"
SECONDS_BETWEEN_CALLS = 12  # Limit to don't hit the rate limit call per minute. More info  in the endpoint's FAQ


class DataRetrieval:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date
        self._data_ingestion = DataIngestion()

    def _week_generator(self):
        current_date = self.start_date

        while current_date < self.end_date:
            yield current_date
            current_date = current_date + timedelta(days=6)
            current_date = (
                self.end_date if current_date > self.end_date else current_date
            )

    def _request_data(self, published_date: str) -> Any:
        params = {"api-key": API_KEY, "published_date": published_date}
        response = requests.get(LISTS_OVERVIEW_ENDPOINT, params=params)

        if response.status_code == 401:
            raise InvalidApiKey

        if response.status_code == 200:
            return response.json()

    def _create_raw_results(self, content: dict[str, Any]) -> RawResults:
        raw_results = RawResults(
            results_id=str(uuid4()),
            status=content["status"],
            copyright=content["copyright"],
            num_results=content["num_results"],
            bestsellers_date=content["results"]["bestsellers_date"],
            published_date=content["results"]["published_date"],
            created_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        )
        return raw_results

    def _create_raw_list(
        self, content: dict[str, Any], raw_results: RawResults
    ) -> RawList:
        raw_list = RawList(
            list_id=content["list_id"],
            results_id=raw_results.results_id,
            list_name=content["list_name"],
            display_name=content["display_name"],
            updated=content["updated"],
            list_image=content["list_image"],
            created_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        )
        return raw_list

    def _create_raw_book(self, content: dict[str, Any], raw_list: RawList) -> RawBook:
        raw_book = RawBook(
            list_id=raw_list.list_id,
            results_id=raw_list.results_id,
            age_group=content["age_group"],
            author=content["author"],
            contributor=content["contributor"],
            contributor_note=content["contributor_note"],
            description=content["description"],
            price=content["price"],
            primary_isbn13=content["primary_isbn13"],
            primary_isbn10=content["primary_isbn10"],
            publisher=content["publisher"],
            rank=content["rank"],
            title=content["title"],
            created_date=content["created_date"],
            updated_date=content["updated_date"],
            created_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        )
        return raw_book

    def run(self):
        """
        Execute the process responsible from getting the lists of books from
        The New York Time API. It downloads the data from the provided date interval
        and stores it into a PostgreSQL database.
        """
        for week in self._week_generator():
            last_request_time = time.time()
            published_date = week.strftime(DATE_FORMAT)
            print(f"Requesting data for {published_date}")
            content = self._request_data(published_date)

            print("Ingesting raw results.")
            raw_results = self._create_raw_results(content)
            self._data_ingestion.ingest_raw([raw_results], "raw_results")

            print("Ingesting raw lists.")
            raw_lists = []
            for list_content in content["results"]["lists"]:
                raw_list = self._create_raw_list(list_content, raw_results)
                raw_lists.append(raw_list)

                print(f"Ingesting raw books from list {raw_list.list_id}")
                raw_books = []
                for book_content in list_content["books"]:
                    raw_book = self._create_raw_book(book_content, raw_list)
                    raw_books.append(raw_book)
                self._data_ingestion.ingest_raw(raw_books, "raw_books")

            self._data_ingestion.ingest_raw(raw_lists, "raw_lists")

            time_diff = time.time() - last_request_time

            if time_diff <= SECONDS_BETWEEN_CALLS:
                time.sleep(SECONDS_BETWEEN_CALLS - time_diff)
