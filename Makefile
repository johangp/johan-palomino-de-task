.PHONY: up

up:
	docker compose up -d --build

down:
	docker compose down

ingestion:
	docker run --network johan-palomino-de-task_app_network -it de-task uv run python -m ingestion.cli 2021-01-01 2023-12-31

dbt-run:
	docker run --network johan-palomino-de-task_app_network --rm -it de-task uv run dbt run

dbt-test:
	docker run --network johan-palomino-de-task_app_network --rm -it de-task uv run dbt test

test:
	pytest tests/
