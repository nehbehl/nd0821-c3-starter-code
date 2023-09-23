from typing import Union, List
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel


class Data(BaseModel):
    age: int
    workclass: str
    relationship: str


app = FastAPI(
    title="Exercise API",
    description="An API that demonstrates checking the values of your inputs.",
    version="1.0.0",
)

@app.get("/")
async def say_hello():
    return {"Hello to Udacity Machine Learning Devops ND"}

@app.post("/data/")
async def ingest_data(data: Data):
    if data.age == 0:
        raise HTTPException(status_code=400, detail="age needs to be above 0.")

    return data
