from datamodel.cart import CartDetails, ProductDetails
from datamodel.entity import CartEntity, ProductEntity
from exception.customexception import ApplicationException
from log.logger import logger
from client.productclient import ProductClient
import asyncio

class CartService:

    def __init__(self):
        """This class use a dictionary where the Key is the id and the Value is the ProductDetails object"""
        self.product_client = ProductClient(base_url="http://localhost:8092")
        self.user_id_cart_storage: dict[int, CartEntity] = {}
        self.pre_existing_records()

    def pre_existing_records(self):
        logger.debug("Initializing pre existing records for users")
        self.user_id_cart_storage[101] = CartEntity(
            id = 1,
            user_id = 101, 
            products = [ProductEntity(id = 1001, quantity = 2), ProductEntity(id = 1003, quantity = 1)]
        )
        self.user_id_cart_storage[102] = CartEntity(
            id = 2,
            user_id = 102, 
            products = [ProductEntity(id = 1002, quantity = 3), ProductEntity(id = 1003, quantity = 2)]
        )

    # --- GET ---
    async def get_by_user_id(self, user_id: int) -> CartDetails:
        """Return the cart for the user"""
        if user_id not in self.user_id_cart_storage:
            logger.info("No cart details found for the user id: %s", user_id)
            self.user_id_cart_storage[user_id] = CartEntity(id = user_id, user_id = user_id, products = [])
            return CartDetails(user_id = user_id, total_price = 0.0, products = [])
        cart_entity = self.user_id_cart_storage.get(user_id)
        logger.info("Cart details for the user %s is %s", user_id, cart_entity)
        return await self.build_cart_with_products(cart_entity)

    async def build_cart_with_products(self, cart_entity: CartEntity) -> CartDetails:
        total = 0.0
        product_list = []
        for product_entity in cart_entity.products:
            product_details = await self.product_client.get_product_details(product_entity.id)
            if product_details:
                product_details.quantity = product_entity.quantity
                total += (product_details.price * product_details.quantity)
                product_list.append(product_details)
        return CartDetails(user_id = cart_entity.user_id, total_price = total, products = product_list)       

    # Add product or more quantity to the cart for given user
    async def add_to_cart(self, user_id: int, product: ProductDetails) -> CartDetails:
        """Add new product or more quantity to the cart"""
        cart = self.user_id_cart_storage.get(user_id)
        
        # Safety check: Create cart if it doesn't exist
        if not cart:
             cart = CartEntity(id=user_id, user_id=user_id, products=[])
             self.user_id_cart_storage[user_id] = cart

        logger.info("Adding %d quantity to product id '%d' for the user %s", product.quantity, product.id, user_id)
        
        found = False
        for cart_product in cart.products:
            if product.id == cart_product.id:
                cart_product.quantity += product.quantity
                found = True
                break
        
        if not found:
            cart.products.append(ProductEntity(id = product.id, quantity = product.quantity))
            
        self.user_id_cart_storage[user_id] = cart
        return await self.get_by_user_id(user_id)
    
    # Delete from cart - either complete product or reduce quantity
    async def delete_from_cart(self, user_id: int, product: ProductDetails) -> CartDetails:
        """Delete product or quantity from the cart"""
        cart = self.user_id_cart_storage.get(user_id)
        
        # Safety: If cart doesn't exist, just return the empty state
        if not cart:
            logger.warning(f"User {user_id} tried to delete from non-existent cart")
            return await self.get_by_user_id(user_id)

        logger.info("Deleting %d quantity from product id '%d' for the user %s", product.quantity, product.id, user_id)
        
        for cart_product in cart.products:
            if product.id == cart_product.id:
                if product.quantity >= cart_product.quantity:
                    cart.products.remove(cart_product)
                else:
                    cart_product.quantity -= product.quantity
                break

        self.user_id_cart_storage[user_id] = cart
        return await self.get_by_user_id(user_id)
    