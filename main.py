from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World! How are you harsha"}

# Example of a POST endpoint
@app.post("/submit")
def submit_data(data: dict):
    return {"received_data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
