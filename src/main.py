from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A context-aware Git assistant using LangGraph and FastAPI",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping", tags=["Health"])
async def ping() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        dict: A simple response indicating the service is running
    """
    return {"message": "pong"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT) 