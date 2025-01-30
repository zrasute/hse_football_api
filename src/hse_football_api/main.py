import uvicorn
from fastapi import FastAPI

from hse_football_api.api import router as api_router
from hse_football_api.core.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.api.prefix)


if __name__ == "__main__":
    uvicorn.run(
        "hse_football_api.main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
