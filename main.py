import requests
import ast
import uvicorn
from datetime import datetime
from fastapi import FastAPI, status
from starlette.requests import Request
from starlette.responses import Response


class Product:
    def __init__(self, type, value, qty):
        self.type = type
        self.value = value
        self.qty = qty
        
    def __str__(self) -> str:
        return f"""Type:{self.type}
            | Value: {self.value} | Quantity:{self.qty}"""
        
class Customer:
    def __init__(self, document, name) -> None:
        self.document = document
        self.name = name
        
    def validate_cpf(self):
        cpf = self.document
        if len(cpf) < 11:
            return False    
        
        if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
            return False
        
        calc = [i for i in range(1, 10)]
        d1= (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
        d2= (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10
        return str(d1) == cpf[-2] and str(d2) == cpf[-1]
    
    def __str__(self):
        return f"""Document: {self.document} | Name {self.name}"""
    

class Order:
    def __init__(self, sold_at, customer:Customer, total):
        datetime_obj = datetime.strptime(sold_at,'%y/%m/%d %H:%M:%S')
        self.customer = customer
        self.sold_at = datetime_obj
        self.total = total
        self.products = []
        
    def append_product(self,type, value, qty):
        product = Product(type, value, qty)
        self.products.append(product)
        
        
    

app = FastAPI()


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
    
    if(customer.validate_cpf() is False):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status":"document invalid"
        }
    
    order = Order(customer=customer, sold_at=order_data["sold_at"], total=order_data["total"])
    
    total_order = 0
        
    for product in order_data["products"]:
        order.append_product(Product(product["type"], product["value"], product["qty"]))
        total_order =+ product["value"]
    
    
    if(total_order != order.total):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status":"Value order is not equal to total products value"
        }
    
    return {
        "status":"Error"
    }



