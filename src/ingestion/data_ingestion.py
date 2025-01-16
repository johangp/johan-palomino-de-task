import psycopg2

from .ddl import raw_results_ddl


class DataIngestion:
    def __init__(self):
        self._conn = psycopg2.connect(
            database="new_york_times",
            user="deel",
            password="deel",
            host="localhost",
            port="5432",
        )
        self._provision_ddl_commands()

    def _provision_ddl_commands(self):
        self._conn.autocommit = True
        cursor = self._conn.cursor()

        cursor.execute(raw_results_ddl)
        print("Raw results DDL executed successfully.")

        self._conn.commit()
        self._conn.close()
