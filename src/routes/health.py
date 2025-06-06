from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
    responses={404: {"description": "Not found"}},
)

@router.get("/ping")
async def ping() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        dict: A simple response indicating the service is running
    """
    return {"message": "pong"} 