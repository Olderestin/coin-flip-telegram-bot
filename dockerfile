FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/temp/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/temp/requirements.txt

WORKDIR /bot
COPY . .


ENTRYPOINT [ "python", "-m", "bot" ]