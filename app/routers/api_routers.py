from .v1 import (
    system_routes
)
from fastapi import APIRouter


router = APIRouter()


router.include_router(
    router=system_routes,
    prefix="/api/v1",
)
