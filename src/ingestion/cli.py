from datetime import datetime

import typer

app = typer.Typer()


@app.command()
def ingestion(start_date: datetime, end_date: datetime):
    print(f"Hello {start_date}")
    print(f"Hello {end_date}")


if __name__ == "__main__":
    app()
