FROM python:3.8.5-slim-buster

WORKDIR /bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
