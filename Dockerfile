FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements-dev.txt

CMD ["uvicorn", "app.routes:app", "--host", "0.0.0.0", "--port", "80"]