from fastapi import FastAPI
from app.api.v1.routes import router as v1_router

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application demonstrating basic setup.",
    version="1.0.0"
)

app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "API is running 🎉"}