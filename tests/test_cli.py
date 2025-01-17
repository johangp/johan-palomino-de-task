from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
from typer.testing import CliRunner

from src.ingestion.cli import app

runner = CliRunner()


@pytest.fixture()
def mock_data_retrieval(mocker: MockFixture) -> Mock:
    mock = mocker.patch("src.ingestion.cli.DataRetrieval")
    return mock


def test_ingestion_succeeds(mock_data_retrieval: Mock):
    result = runner.invoke(app, ["2021-01-01", "2023-01-01"])

    assert result.exit_code == 0


def test_ingestion_fails_wrong_format(mock_data_retrieval: Mock):
    result = runner.invoke(app, ["202101-01", "202-01-1"])

    assert result.exit_code > 0
