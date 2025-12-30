class ProductEntity:

    id: int
    quantity: int
    
    def __init__(self, id: int, quantity: int):
        self.id = id
        self.quantity = quantity

    # Override this method to define custom string representation like toString() method in Java
    def __str__(self):
        return f"ProductEntity[id = {self.id}, quantity = {self.quantity}]"
    
    # Used when printing a LIST of objects: print([obj1, obj2])
    def __repr__(self):
        return self.__str__()


class CartEntity:
    
    id: int
    user_id: int
    products: list[ProductEntity]
    
    def __init__(self, id: int, user_id: int, products: list[ProductEntity]):
        self.id = id
        self.user_id = user_id
        self.products = products

    # Override this method to define custom string representation like toString() method in Java
    def __str__(self):
        return f"CartEntity[id = {self.id}, user_id = {self.user_id}, products = {self.products}]"
    

