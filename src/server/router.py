from fastapi import APIRouter
from datamodel.cart import CartDetails, ProductDetails
from datamodel.response import GenericResponse
from service.cartsvc import CartService

# This is the API router similar to Springboot controller
cart_router = APIRouter(prefix="/cart-ms", tags= ["cart"])

cart_service = CartService()

# Get product by User Id
@cart_router.get("/v1/cart/user/{user_id}", description="Get cart details by user id")
async def get_by_product_id(user_id: int) -> GenericResponse[CartDetails]:
    product = cart_service.get_by_user_id(id)
    return GenericResponse.success(product)

# Add product in the cart
@cart_router.post("/v1/add-to-cart/{user_id}", description="Add product to cart")
async def add_to_cart(user_id: int, product: ProductDetails) -> GenericResponse[CartDetails]:
    product = cart_service.add_to_cart(id, product)
    return GenericResponse.success(product)

# Delete product from the cart
@cart_router.post("/v1/delete-from-cart/{user_id}", description="Delete product from cart")
async def delete_from_cart(user_id: int, product: ProductDetails) -> GenericResponse[CartDetails]:
    product = cart_service.substract_quantity(id, product)
    return GenericResponse.success(product)
