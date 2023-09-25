from typing import Union, List
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel, Field

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sys
from pathlib import Path
import pickle
import pandas as pd

cwd = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, cwd)


# Add the necessary imports for the starter code.
import starter
import starter.starter
import starter.starter.ml
import pandas as pd
from starter.starter.ml.data import process_data
from starter.starter.ml.model import train_model, compute_model_metrics, inference
import numpy as np
import math
import pytest


# Add code to load in the data.
data = pd.read_csv('./starter/starter/clean_census.csv')


# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)
# Process the test data with the process_data function.
X_test, y_test, encoder_t, lb_t = process_data(
        test, categorical_features=cat_features,
        label="salary", training=False, encoder=encoder, lb=lb)

# Train and save a model.
model = train_model(X_train, y_train)

predictions = inference(model, X_test)




class Data(BaseModel):
    sno: int = Field(..., example=0)
    age: int = Field(..., example=39)
    workclass: str = Field(..., example="State-gov")
    education: str = Field(..., example="Bachelors")
    marital_status: str = Field(..., alias="marital-status", example="Never-married")
    occupation: str = Field(..., example="Adm-clerical")
    relationship: str = Field(..., example="Not-in-family")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    hours_per_week: int = Field(..., alias="hours-per-week", example=40)
    native_country: str = Field(
        ..., alias="native-country", example="United-States"
    )


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

@app.post("/predict/")
async def predict(data: Data):
    cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country"
]
    datadf = pd.DataFrame(data = [data.dict(by_alias=True)], index = [0])
    datadf,_,_,_ = process_data(datadf, cat_features, label=None, training=False, encoder=encoder, lb=lb)
    pred = inference(model, datadf)

    if pred[0]:
        pred = {'salary': '>50k'}
    else:
        pred = {'salary': '<=50k'}
    return pred
    
