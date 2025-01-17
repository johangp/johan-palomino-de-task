# DE-Task

The repository is structured in two main parts: The `src` folder which contains the Python code to perform the Data retrieval and the `new_york_times` folder which includes a dbt project to perform
all the dimensional modeling tasks including the requested SQL queries. The CSV output can be found in the `results` folder.

The ingestion consists in a Python cli app that request the data to the NYT endpoint and stored it in a PosgreSQL database. The data is stored in three raw models: `raw_results`, `raw_lists` and `raw_books`.
These models contain duplicated data because this approach aims to have the data closest to the endpoint to avoid reprocessing steps. 

I built the dimensional and fact models using dbt from these raw models. You can see the data lineage graph here:

![image](https://github.com/user-attachments/assets/fee75142-8c2c-42ed-8edf-122764b058ca)

DBT models can be found in `new_york_times/models`.

## How to run it:

### Pre-requisites:

- Docker and docker compose install
- [uv](https://docs.astral.sh/uv/) Python package manager (optional if you want to run the Python tests)

### Run it:

- `make up`: command will build the needed Docker image to run the ingestion process and the dbt command. It also ups a PostgreSQL instance.
- `make ingestion`: Will run the Python process to perform the data retrieval. By default will ingest data from 2021 to 2023. You can change the start-date and end-date in the Make command.
- `make dbt-run`: Once the date is loaded into the database, you can perform the dbt run to generate the data models.
- `make dbt-test`: Make sure that the data is correct by running the dbt tests.
- `make test`: Run the unittest for the Python base code. For this step is needed that you have install the project dependencies into a Python environment. You can do it by running `uv sync`.

Using your prefered database client, you can connect to the database to check that the ingestion process is ok or to review the data models. Details for the connection:

      dbname: new_york_times
      host: localhost
      pass: deel
      port: 5432
      schema: public
      user: deel
