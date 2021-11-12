FROM python:3

WORKDIR /app

COPY . /app

EXPOSE 8000

RUN pip install -r requirements-dev.txt

CMD ["uvicorn" , "main:app"]