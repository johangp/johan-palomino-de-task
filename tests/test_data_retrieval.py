from datetime import datetime

from src.ingestion.data_retrieval import DataRetrieval


def test_data_retrieval_loads():
    start_date = datetime.strptime("2021-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-01-01", "%Y-%m-%d")

    data_retrieval = DataRetrieval(start_date, end_date)

