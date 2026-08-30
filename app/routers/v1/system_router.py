from fastapi import APIRouter


router = APIRouter(
    tags=["System"],
    prefix="/system",
)


@router.get(
    "/health",
    summary="Health Check Endpoint",
    response_description="Returns the health status of the application.",
    response_model=dict
)
async def health_check():
    """
    Health check endpoint to verify that the application is running.

    Returns:
        dict: A dictionary containing the health status of the application.
    """
    return {"status": "healthy"}
