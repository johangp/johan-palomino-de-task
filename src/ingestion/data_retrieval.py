import time
from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from .data_ingestion import DataIngestion
from .data_models import RawResults
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

        while current_date <= self.end_date:
            yield current_date
            current_date = current_date + timedelta(days=6)
            current_date = (
                self.end_date if current_date > self.end_date else current_date
            )

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(SECONDS_BETWEEN_CALLS))
    def _request_data(self, published_date: str) -> Any:
        params = {"api-key": API_KEY, "publisd_date": published_date}
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

    def run(self):
        """
        Execute the process responsible from getting the lists of books from
        The New York Time API. It downloads the data from the provided date interval
        and stores it into a PostgreSQL database.
        """
        for week in self._week_generator():
            last_request_time = time.time()
            content = self._request_data(week.strftime(DATE_FORMAT))

            raw_results = self._create_raw_results(content)
            self._data_ingestion.ingest_raw_results(raw_results)

            time_diff = time.time() - last_request_time

            if time_diff <= SECONDS_BETWEEN_CALLS:
                time.sleep(SECONDS_BETWEEN_CALLS - time_diff)
