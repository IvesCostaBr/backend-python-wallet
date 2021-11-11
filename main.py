from fastapi import FastAPI, status
from starlette.requests import Request
import requests
import ast

from starlette.responses import Response

app = FastAPI()


@app.get("/")
async def index():
    return {
        "Cashback Processing Software V:": 1.1,
        "Dev":"Ives Costa",
        "Date":""
    }




@app.post("/api/cashback", status_code=201)
async def cashback_processor(request: Request, response :Response):
    #Converting Bytes in to Dict
    data_receiver = await request.body()
    dict_data = data_receiver.decode("UTF-8")
    order_data = ast.literal_eval(dict_data)
    
    
    
    return {
        "status":"Error"
    }