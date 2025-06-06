from fastapi import FastAPI
from .health import router as health_router

def register_routes(app: FastAPI) -> None:
    """
    Register all route modules with the FastAPI application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.include_router(health_router) 