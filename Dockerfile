
FROM python:3.12-alpine3.20

RUN mkdir /bot
WORKDIR /bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "main.py", "run"]
