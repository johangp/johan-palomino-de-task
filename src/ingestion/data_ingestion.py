import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from .ddl import raw_results_ddl

CONN_ARGS = {
    "database": "new_york_times",
    "user": "deel",
    "password": "deel",
    "host": "localhost",
    "port": "5432",
}


class DataIngestion:
    def __init__(self):
        self._conn = psycopg2.connect(**CONN_ARGS)  # type: ignore
        self._provision_ddl_commands()

    def _provision_ddl_commands(self):
        self._conn.autocommit = True
        cursor = self._conn.cursor()

        cursor.execute(raw_results_ddl)
        print("Raw results DDL executed successfully.")

        self._conn.commit()
        self._conn.close()

    def ingest_raw_results(self, df: pd.DataFrame):
        engine = create_engine(URL.create(**CONN_ARGS))  # type: ignore

        df.to_sql("raw_results", engine)
