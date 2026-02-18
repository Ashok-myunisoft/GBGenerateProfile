from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Profile Generator")

app.include_router(router, prefix="/api")
