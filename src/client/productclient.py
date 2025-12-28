import httpx
from datamodel.cart import ProductDetails
from log.logger import logger

class ProductClient:
    def __init__(self, base_url: str = "http://localhost:8092"):
        self.base_url = base_url

    async def get_product_details(self, product_id: int) -> ProductDetails | None:
        """
        Calls Product-MS: GET /product-ms/v1/product/{id}
        """
        url = f"{self.base_url}/api/product-ms/v1/product/{product_id}"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                
                if response.status_code == 200:
                    # Parse the JSON response
                    # Expected format: {"isSuccess": true, "payload": {...}}
                    json_data = response.json()
                    
                    if json_data.get("isSuccess"):
                        payload = json_data.get("payload")
                        # Convert dict to Pydantic Object
                        return ProductDetails(**payload)
                
                logger.warning(f"Product MS returned {response.status_code} for ID {product_id}")
                return None

            except Exception as e:
                logger.error(f"Failed to call Product MS: {str(e)}")
                return None