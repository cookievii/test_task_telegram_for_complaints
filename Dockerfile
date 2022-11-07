FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /bot

COPY poetry.lock pyproject.toml ./

RUN apk add --no-cache --virtual make gcc g++

RUN pip install poetry

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD python telegram_bot.py