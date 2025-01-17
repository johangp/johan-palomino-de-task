FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

ADD . /app

COPY new_york_times/profiles.yml /root/.dbt/profiles.yml

WORKDIR /app

RUN uv sync --frozen
RUN uv pip install .

WORKDIR /app/new_york_times

