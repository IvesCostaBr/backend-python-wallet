from fastapi import FastAPI, status
from starlette.requests import Request
from starlette.responses import Response
from models import Customer, Order
from consts import *
import httpx
import ast
import uvicorn
import json



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
        response.status_code = 400
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
        response.status_code = 400
        return {
            "status":"Value order error"
        }
        
    #Send cashback for API
    
    try:   
        response_api = httpx.post(url=API_URL_REQUEST,
                    data=json.dumps({
            "document":order.customer.document,
            "cashback":order.calculation_cashback_products()
        })).json()
        status = "Cashback complete"
        response.status_code = 201
    except:
        response_api="error in request"
        status = "Operation Fail"
        response.status_code = 500
    
        
    #Response to client
    return {
        "status":status,
        "response":response_api
    }


if __name__ == '__main__':
    uvicorn.run(app="main:app",host="127.0.0.1",port=8000,debug=True)