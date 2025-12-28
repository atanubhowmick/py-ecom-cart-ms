from fastapi import FastAPI
from server.router import cart_router
from exception.customexception import ApplicationException
from exception.handler import global_exception_handler

app = FastAPI()
app.include_router(cart_router, prefix="/api")
app.add_exception_handler(ApplicationException, global_exception_handler)
