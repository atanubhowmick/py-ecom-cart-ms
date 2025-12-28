from datamodel.cart import CartDetails, ProductDetails
from datamodel.entity import CartEntity, ProductEntity
from exception.customexception import ApplicationException
from log.logger import logger
from client.productclient import ProductClient
import asyncio

class CartService:

    def __init__(self):
        """This class use a dictionary where the Key is the id and the Value is the ProductDetails object"""
        self.user_id_cart_storage: dict[int, CartEntity] = {}
        self.pre_existing_records()

    def pre_existing_records(self):
        logger.debug("Initializing pre existing records for users")
        self.user_id_cart_storage[1] = CartEntity(
            user_id = 1, 
            product_ids = list(ProductEntity(1001, 2), ProductEntity(1003, 1))
        )
        self.user_id_cart_storage[2] = CartEntity(
            user_id = 2, 
            product_ids = list(ProductEntity(1002, 3), ProductEntity(1003, 2))
        )

    # --- GET ---
    async def get_by_user_id(self, user_id: int) -> CartDetails:
        """Return the cart for the user"""
        if id not in self.user_id_cart_storage:
            self.user_id_cart_storage[user_id] = CartDetails(user_id, 0.0, list())
        cart_entity = self.product_storage.get(user_id)
        # iterate over product enitiy list and get all the product details. 
        # Build Cart Details with product details
        # and return complete cart details
        for product_entity in cart_entity.products:
            # Call Microservice
            product_info = await self.product_client.get_product_details(product_entity.id)
        
    # def get_product_details(self, product_id):
        
    
    def add_to_cart(self, user_id: int, product: ProductDetails) -> ProductDetails:
        """Add new product or more quantity to the cart"""
        cart = self.user_id_cart_storage(user_id)
        
        # Lazy formatting inside logger
        logger.info("Adding %d quantity to product id '%d'. Current quantity: %s", quantity, id, product.available_qty)
        return self.update(product)
    
    def substract_quantity(self, id: int, quantity: int) -> ProductDetails:
        """Delete the or reduce quantity in the cart"""
        product = self.get_by_id(id)
        if quantity > product.available_qty:
            raise ProductException("E003", f"Can't dispence {quantity} quantity from product id '{id}'. Available quantity: {product.available_qty}", 400)
        product.available_qty -= quantity
        # Eager formatting using string formatter
        logger.info(f"Reducing {quantity} qyantity from product id '{id}'. Current quantity: {product.available_qty}")
        return self.update(product)
    