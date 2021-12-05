import uvicorn
from fastapi import FastAPI
from api.routes import helpers, tracks, metrics
from api.repositories.db import DataBase
app = FastAPI()
DataBase()

app.include_router(helpers.router)
app.include_router(tracks.router)
app.include_router(metrics.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")