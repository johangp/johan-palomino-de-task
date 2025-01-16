from datetime import datetime
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

from src.ingestion.data_retrieval import DataRetrieval


@pytest.fixture()
def data_retrieval() -> DataRetrieval:
    start_date = datetime.strptime("2021-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
    return DataRetrieval(start_date, end_date)


@pytest.fixture()
def mock_requests_get(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    return mock


def test_data_retrieval_request_data_invokes_requests_get(
    data_retrieval: DataRetrieval, mock_requests_get: Mock
):
    data_retrieval._request_data("2021-01-01")
    assert mock_requests_get.called
