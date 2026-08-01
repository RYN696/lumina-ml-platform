from fastapi import FastAPI

app = FastAPI(
    title="Lumina",
    description="End-to-End ML platform",
    version="0.1"
)

@app.get("/")
def home():
    return {
        "message":"Lumina platform is running"
    }