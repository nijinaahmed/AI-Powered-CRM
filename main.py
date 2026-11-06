from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered CRM",
    description="Customer and Sales Assistant API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to AI-Powered CRM"}