from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from configs import ai_agent_config
from routes import register_routes


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

    # Register all routes
    register_routes(app)
    
    return app


app = create_app()