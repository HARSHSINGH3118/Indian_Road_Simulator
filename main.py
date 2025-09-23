from fastapi import FastAPI
import uvicorn

# Create FastAPI app
app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "Your server is live"}

# Entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
