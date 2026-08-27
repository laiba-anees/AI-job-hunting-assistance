from fastapi import FastAPI

app = FastAPI(title="AI Job Hunting Assistant")


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