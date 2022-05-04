FROM python:3.8.5-slim-buster

WORKDIR /bot

RUN apt-get update && \
  apt-get install -y \
  build-essential \
  libcairo2-dev \
  pkg-config

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
