from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datamodel.response import GenericResponse
from exception.customexception import ApplicationException
from log.logger import logger

# Global exception handler
async def global_exception_handler(request: Request, exception: ApplicationException):
    logger.error(
        "Application Exception occurred with error code: %s and message: %s", 
        exception.error_code, 
        exception.error_message,
        exc_info = True
    )
    response =  GenericResponse.failure(exception.error_code, exception.error_message)
    return JSONResponse(
        status_code = exception.http_status_code,
        content = jsonable_encoder(response)
    )