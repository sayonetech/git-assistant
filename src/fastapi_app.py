from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from configs import ai_agent_config


def create_app():

    app = FastAPI(
        title=ai_agent_config.APPLICATION_NAME,
        description="A context-aware Git assistant using LangGraph and FastAPI",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
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
    return app


app = create_app()