import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.title = "Metadata Dashboard"

@app.get("/")
async def root():
    return {"message": "Hello Metadata"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)