FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH=/code/
WORKDIR /code
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install poetry
COPY poetry.lock /code/
COPY pyproject.toml /code/
RUN poetry install
COPY . /code/


