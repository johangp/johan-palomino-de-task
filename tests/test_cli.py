from typer.testing import CliRunner

from src.ingestion.cli import app

runner = CliRunner()


def test_ingestion_succeeds():
    result = runner.invoke(app, ["2021-01-01", "2023-01-01"])

    assert result.exit_code == 0

def test_ingestion_fails_wrong_format():
    result = runner.invoke(app, ["202101-01", "202-01-1"])

    assert result.exit_code > 0
