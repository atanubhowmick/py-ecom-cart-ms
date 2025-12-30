from pydantic import BaseModel

class ProductDetails(BaseModel):

    # Pydantic requires fields to be defined as class attributes with type hints
    id: int
    name: str
    details: str
    price: float
    available_qty: int
    quantity: int = 0

    # Override this method to define custom string representation like toString() method in Java
    def __str__(self):
        return f"[id = {self.id}, name = {self.name}, available_qty = {self.available_qty}]"

class CartDetails(BaseModel):

    # Pydantic requires fields to be defined as class attributes with type hints
    user_id: int
    total_price: float
    products: list[ProductDetails]

    # Override this method to define custom string representation like toString() method in Java
    def __str__(self):
        return f"[id = {self.id}, name = {self.name}, available_qty = {self.available_qty}]"
