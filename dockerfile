FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /temp/requirements.txt
RUN mkdir -p /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt