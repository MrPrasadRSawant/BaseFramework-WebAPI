from fastapi import FastAPI
from app.routers import all_router_collection


app = FastAPI(
    title="Base Framework for FastAPI Applications",
    summary=(
        "A foundational framework for building FastAPI applications with essential features "
        "like authentication, database integration, and API documentation."
    ),
    description=(
        "This framework provides a structured foundation for developing FastAPI applications, "
        "including features such as authentication, database integration, and API documentation. "
        "It is designed to help developers quickly set up and maintain robust web APIs."
    ),
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
)

app.include_router(router=all_router_collection)
