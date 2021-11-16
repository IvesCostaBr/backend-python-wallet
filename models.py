from datetime import datetime


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


class Product:
    def __init__(self, type, value, qty):
        self.type = type
        self.value = value
        self.qty = qty
        self.discount = 0.00
        

    def __str__(self) -> str:
        return f"""Type:{self.type}
            | Value: {self.value} | Quantity:{self.qty}"""
        
        
    def validate_type(self):   
        allowed_types = {"a":5, "b":15, "c":25}
        if str(self.type).lower() in allowed_types: 
            self.discount = (allowed_types[str(self.type).lower()] / 100) * (self.qty * float(self.value))
            return self.discount
        else:
            return None
        

class Order:
    def __init__(self, sold_at, customer:Customer, total):
        self.sold_at = self.validate_date(sold_at)
        if self.sold_at is None:
            return
        self.customer = customer
        self.total = total
        self.products = []
        self.total_cashback = 0.00
        self.types = []
        
    
    def validate_date(self, date):
        date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if (str(date_time_obj) <= date_now):
            return date_time_obj
        else:
            print("not valid")
            return None
        
        
    def append_product(self,type, value, qty):
        product = Product(type, value, qty)
        self.products.append(product)
        
    def calculation_cashback_products(self):
        for product in self.products:
            value = product.validate_type()
            if (value):
                self.total_cashback += value
            else:
                self.total_cashback = None
                break
    
        return self.total_cashback