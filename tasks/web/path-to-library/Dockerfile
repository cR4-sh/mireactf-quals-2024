FROM python:3.9-slim

RUN apt-get update &&  apt -y upgrade 

WORKDIR /app

COPY app /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python3","server.py"]
