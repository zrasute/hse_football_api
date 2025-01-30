import uvicorn
from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        "hse_football_api.main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
