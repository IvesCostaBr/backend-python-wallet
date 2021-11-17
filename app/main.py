from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from .models import Customer, OrderP
from .consts import *
from .database.orm import Session, Order
import httpx
import ast
import json

app = FastAPI()

#Index
@app.get("/")
async def index():
    return {
        "Cashback Processing Software V:": 1.1,
        "Dev":"Ives Costa",
        "Date":"16/11/2021"
    }


@app.post("/api/cashback")
async def cashback_processor(request: Request, response :Response):
    #Converting Bytes in to Dict
    try:
        data_receiver = await request.body()
        dict_data = data_receiver.decode("UTF-8")
        order_data = ast.literal_eval(dict_data)
    except:
        response.status_code = 400
        return {
            "status":"operation not valid"
        }
    
    customer = Customer(order_data["customer"]["document"], order_data["customer"]["name"])
    
    #Validation CPF
    if(customer.validate_cpf() is False):
        response.status_code = 422
        return {
            "status":"document invalid"
        }

    order = OrderP(customer=customer, 
                  sold_at=order_data["sold_at"], 
                    total=order_data["total"])
    if order.sold_at == None:
        response.status_code = 422
        return {
            "status":"Date invalid"
        }
    
    total_order = 0
    for product in order_data["products"]:
        count = 0
        order.append_product(type=product["type"], 
                                value=product["value"], 
                                    qty=product["qty"])
        if order.products[count].type == None:
            response.status_code == 400
            return {
                "status":"type error"
            }
        total_order += (float(product["value"]) * product["qty"])
        count += count
     
    #Validation Total Order
    if(float(total_order) != float(order.total)):
        response.status_code = 422
        return {
            "status":"Value order error"
        }
        
    #Send cashback for API  
    try:      
        response_api = httpx.post(url=API_URL_REQUEST,
                    data=json.dumps({
            "document":order.customer.document,
            "cashback":order.calculate_cashback_products()
        })).json()
        
        status = "Cashback complete"
        response.status_code = 201
        try:
            order.save_order() 
        except:
            print("Error save database")
            
    except:
        response_api="error in request"
        status = "Operation Fail"
        response.status_code = 500
        
     
    #Response to client
    return {
        "status":status,
        "response":response_api
    }
    
    
#get all register    
@app.get("/api/cashback")
async def cashbash_get():
    database_session = Session()
    orders = database_session.query(Order).all()
    response_list = []
    
    for order in orders:
        response_list.append(order.return_dict())
    
    print(response_list)
    json_resp = json.dumps(response_list)
    return json_resp