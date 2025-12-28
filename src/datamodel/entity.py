class ProductEntity:

    id: int
    quantity: int
    
    def __init__(self, id: int, quantity: int):
        self.id = id
        self.quantity = quantity

    # Override this method to define custom string representation like toString() method in Java
    def __str__(self):
        return f"ProductEntity[id = {self.id}, quantity = {self.quantity}]"


class CartEntity:

    user_id: int
    products: list[ProductEntity]
    
    def __init__(self, id: int, user_id: int, products: list[ProductEntity]):
        self.id = id
        self.user_id = user_id
        self.products = products

    # Override this method to define custom string representation like toString() method in Java
    def __str__(self):
        return f"CartEntity[id = {self.id}, user_id = {self.user_id}, products = {self.products}]"
    

