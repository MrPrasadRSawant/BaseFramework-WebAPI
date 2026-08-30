from fastapi import APIRouter, Response
from ...schemas import (
    HealthResponse
)
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

router = APIRouter(
    tags=["System"],
    prefix="/system",
)


@router.get(
    "/health",
    summary="Health Check Endpoint",
    response_description="Returns the health status of the application.",
    response_model=HealthResponse
)
async def health_check():
    """
    Health check endpoint to verify that the application is running.

    Returns:
        dict: A dictionary containing the health status of the application.
    """
    return HealthResponse(
        status="OK",
        version_major=1,
        version_minor=0,
        version_patch=0
    )


@router.get(
    "/metrics",
    summary="Get application metrics",
    include_in_schema=True,
)
async def metrics() -> Response:
    """
    Exposes application metrics for Prometheus scraping.
    """
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
