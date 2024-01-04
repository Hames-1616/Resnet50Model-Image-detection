
from typing import Annotated
import uuid
from kerass import predict
from fastapi import FastAPI,File,UploadFile
import uvicorn

app = FastAPI()

db = []

# for Deployment
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000) 

@app.get("/")
async def getpage():
    return "hello"

@app.post("/files")
async def create_upload_file(file: UploadFile = File(...)):
   return await predict(file)
    
    