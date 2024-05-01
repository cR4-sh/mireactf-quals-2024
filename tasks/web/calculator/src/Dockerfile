FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN python3 -m pip install flask

ENTRYPOINT [ "python3", "app.py" ]