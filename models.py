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
        
    

class Order:
    def __init__(self, sold_at, customer, total):
        self.customer = customer
        self.sold_at = sold_at
        self.total = total
        self.products = []
        
    def append_product(self,type, value, qty):
        product = Product(type, value, qty)
        self.products.append(product)
        
    