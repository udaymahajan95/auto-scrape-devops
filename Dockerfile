FROM python:3.12-slim

WORKDIR /app 

COPY application/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY application/ ./application/

CMD ["python", "application/main.py"]
