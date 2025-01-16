import time
from datetime import datetime, timedelta
from typing import Any

import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from .exceptions import InvalidApiKey

LISTS_OVERVIEW_ENDPOINT = "https://api.nytimes.com/svc/books/v3/lists/overview.json"
API_KEY = "H4K4FyQYZKhhlTwLitBhDG5zDjtC2Cib"  # Harcoded for the sake of simplicity
DATE_FORMAT = "%Y-%m-%d"
SECONDS_BETWEEN_CALLS = 12  # Limit to don't hit the rate limit call per minute. More info  in the endpoint's FAQ


class DataRetrieval:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

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

    def run(self):
        """
        Execute the process responsible from getting the lists of books from
        The New York Time API. It downloads the data from the provided date interval
        and stores it into a PostgreSQL database.
        """
        for week in self._week_generator():
            last_request_time = time.time()
            content = self._request_data(week.strftime(DATE_FORMAT))

            # Data ingestion

            time_diff = time.time() - last_request_time

            if time_diff <= SECONDS_BETWEEN_CALLS:
                time.sleep(SECONDS_BETWEEN_CALLS - time_diff)
