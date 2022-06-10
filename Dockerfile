FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements /code/requirements
RUN pip install -r requirements/local.txt
COPY . /code/
