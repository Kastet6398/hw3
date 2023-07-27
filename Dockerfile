FROM python:3.10.3-slim

WORKDIR /app

COPY . .

RUN apt-get update

CMD ["python", "main.py", "10"]
