from fastapi import FastAPI
from starlette.requests import Request
import json
import ast

app = FastAPI()


@app.get("/")
async def index():
    return {
        "Cashback Processing Software V:": 1.1,
        "Dev":"Ives Costa"
    }

@app.post("/api/cashback")
async def cashback_processor(request: Request):
    #Converting Bytes in to Dict
    data_receiver = await request.body()
    dict_data = data_receiver.decode("UTF-8")
    order_data = ast.literal_eval(dict_data)
    
    print(order_data)
    
    return {
        "status":201
    }