from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Job Hunting Assistant",
    description="Backend API for the AI Job Hunting Assistant MVP",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "AI Job Hunting Assistant API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }