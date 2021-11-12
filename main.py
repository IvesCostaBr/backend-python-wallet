import requests
import ast
from datetime import datetime
from fastapi import FastAPI, status
from starlette.requests import Request
from starlette.responses import Response
from .models.models import *



API_URL_EXTERNAL="https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback"

app = FastAPI()

#Index
@app.get("/")
async def index():
    return {
        "Cashback Processing Software V:": 1.1,
        "Dev":"Ives Costa",
        "Date":""
    }


@app.post("/api/cashback")
async def cashback_processor(request: Request, response :Response):
    #Converting Bytes in to Dict
    data_receiver = await request.body()
    dict_data = data_receiver.decode("UTF-8")
    order_data = ast.literal_eval(dict_data)
    
    customer = Customer(order_data["customer"]["document"], order_data["customer"]["name"])
    
    #Validation CPF
    if(customer.validate_cpf() is False):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status":"document invalid"
        }
    
    order = Order(customer=customer, sold_at=order_data["sold_at"], total=order_data["total"])
    
    total_order = 0
    for product in order_data["products"]:
        
        order.append_product(type=product["type"], value=product["value"], qty=product["qty"])
        total_order += (float(product["value"]) * product["qty"])
    
    #Validation Total Order
    if(float(total_order) != float(order.total)):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status":"Value order error"
        }
        
    #Send cashback for API
    requests.post(url=API_URL_EXTERNAL, headers="Content-Type: application/json", data={
        "document":order.customer.document,
        "cashback":order.calculation_cashback_products()
    })
        
    return {
        "status":"Cashback complete"
    }



