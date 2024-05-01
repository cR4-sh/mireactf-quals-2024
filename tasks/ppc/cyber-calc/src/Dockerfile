FROM python:3.9-slim
RUN pip install sympy
WORKDIR /app
COPY app /app
EXPOSE 12345
CMD ["python", "server.py"]
