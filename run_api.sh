#!/bin/bash


python -m venv venv
source ./venv/bin/activate

pip install -r requirements-dev.txt

kill -9 $(lsof -t -i:8000)
python main.py