import uvicorn
from configs import ai_agent_config

if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host=ai_agent_config.BACKEND_APP_BIND_ADDRESS, port=ai_agent_config.BACKEND_APP_PORT, reload=True)