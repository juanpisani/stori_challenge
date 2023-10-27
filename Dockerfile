FROM python:3.11.6-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
