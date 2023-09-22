from fastapi import FastAPI
from typing import Union, List
from pydantic import BaseModel

class Data(BaseModel):
    age: int
    workclass: str 
    education: str
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    hours_per_week: int
    native_country: str

app = FastAPI(
    title="Fast API for ML devops project 3",
    description="An API that implements model inference.",
    version="1.0.0",
)

@app.get("/")
async def say_hello():
    return {"Hello to Udacity Machine Learning Devops ND"}

@app.post("/data/")
async def ingest_data(data: Data):
        data = {  'age': inference.age,
                'workclass': inference.workclass, 
                'education': inference.education,
                'marital-status': inference.marital_status,
                'occupation': inference.occupation,
                'relationship': inference.relationship,
                'race': inference.race,
                'sex': inference.sex,
                'hours-per-week': inference.hours_per_week,
                'native-country': inference.native_country,
                }

        testdf = pd.DataFrame(data, index=[0])

        # apply transformation to sample data
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

        model=model.pkl
        testdf,_,_,_ = process_data(
                                testdf, 
                                categorical_features=cat_features, 
                                training=False, 
                                encoder=encoder, 
                                lb=lb
                                )

        prediction = model.predict(testdf)

        if prediction[0]>0.5:
            prediction = '>50K'
        else:
            prediction = '<=50K', 
            data['prediction'] = prediction



        return data
