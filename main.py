from fastapi import FastAPI, status
from starlette.requests import Request
import requests
import ast
import uvicorn

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
        self.customer = customer
        self.sold_at = sold_at
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




@app.post("/api/cashback", status_code=201)
async def cashback_processor(request: Request, response :Response):
    #Converting Bytes in to Dict
    data_receiver = await request.body()
    dict_data = data_receiver.decode("UTF-8")
    order_data = ast.literal_eval(dict_data)
    
    customer = Customer(order_data["customer"]["document"], order_data["customer"]["name"])
    print(customer.validate_cpf())
    
    
    for product in order_data["products"]:
        print(product)
    
    
    return {
        "status":"Error"
    }



