# DE-Task

The repository is structured in two main parts: The `src` folder which contains the Python code to perform the Data retrieval and the `new_york_times` folder which includes a dbt project to perform
all the dimensional modeling tasks including the requested SQL queries, which the CSV output can be found in the `results` folder.

The ingestion consists in a Python cli app that request the data to the NYT endpoint and stored it in a PosgreSQL database. The data is stored in three raw models: `raw_results`, `raw_lists` and `raw_books`.
These models contain duplicated data because this approach aims to have the data closest to the endpoint to avoid reprocessing steps. 

I built the dimensional and fact models using dbt from these raw models. You can see the data lineage graph here:

![image](https://github.com/user-attachments/assets/fee75142-8c2c-42ed-8edf-122764b058ca)

DBT models can be found in `new_york_times/model`.


## How to run it:

### Pre-requisites:

- 
