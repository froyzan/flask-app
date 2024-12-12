FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt app.py .

RUN pip install -r requirements.txt

EXPOSE 4321

CMD ["python3", "app.py"]

