import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)

class CustomException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

async def custom_exception_handler(request: Request, exc: CustomException):
    logger.error(f"CustomException: {exc.detail}")
    capture_exception(exc)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    capture_exception(exc)
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )