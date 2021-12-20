FROM python:3.9.5-slim-buster

ADD . /app

WORKDIR /app

CMD [ "python3", "app.py" ]