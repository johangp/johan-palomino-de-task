from typer.testing import CliRunner

from src.ingestion.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["Johan"])

    assert result.exit_code == 0
