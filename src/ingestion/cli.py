from datetime import datetime

import typer


from .data_retrieval import DataRetrieval


app = typer.Typer()


@app.command()
def ingestion(start_date: datetime, end_date: datetime):
    data_retrieval = DataRetrieval(start_date, end_date)
    data_retrieval.run()


if __name__ == "__main__":
    app()
