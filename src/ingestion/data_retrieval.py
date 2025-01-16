from datetime import datetime, timedelta
from typing import Any

import requests

LISTS_OVERVIEW_ENDPOINT = "https://api.nytimes.com/svc/books/v3/lists/overview.json"
API_KEY = "H4K4FyQYZKhhlTwLitBhDG5zDjtC2Cib"  # Harcoded for the sake of simplicity


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

    def _request_data(self, published_date: str) -> Any:
        params = {"api-key": API_KEY, "publisd_date": published_date}
        response = requests.get(LISTS_OVERVIEW_ENDPOINT, params=params)

        if response.status_code == 200:
            return response.json()

    def run(self):
        """
        Execute the process responsible from getting the lists of books from
        The New York Time API. It downloads the data from the provided date interval
        and stores it into a PostgreSQL database.
        """
        pass
