from typing import Any

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

from .ddl import raw_books_ddl, raw_lists_ddl, raw_results_ddl

CONN_ARGS = {
    "database": "new_york_times",
    "user": "deel",
    "password": "deel",
    "host": "localhost",
    "port": "5432",
}


class DataIngestion:
    def __init__(self):
        self._engine = create_engine(
            f"postgresql://{CONN_ARGS['user']}:{CONN_ARGS['password']}@{CONN_ARGS['host']}:{CONN_ARGS['port']}/{CONN_ARGS['database']}"
        )
        self._provision_ddl_commands()

    def _provision_ddl_commands(self):
        # Using psycopg2 connection to run DDL as sqlalchemy engine is not working for this purpose. Need to investigate why.
        conn = psycopg2.connect(**CONN_ARGS)  # type: ignore
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(raw_results_ddl)
        print("Raw results DDL executed successfully.")
        cursor.execute(raw_lists_ddl)
        print("Raw lists DDL executed successfully.")
        cursor.execute(raw_books_ddl)
        print("Raw books DDL executed successfully.")

        conn.commit()
        conn.close()

    def ingest_raw(self, raw_values: list[Any], table_name: str):
        df = pd.DataFrame([r.dict() for r in raw_values])
        df.to_sql(table_name, self._engine, if_exists="append", index=False)
