FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /code/storage
COPY . /code/
WORKDIR /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "main.py"]