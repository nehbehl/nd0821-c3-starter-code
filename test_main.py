import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get():
    r = client.get("/")
    assert r.json() == ["Hello to Udacity Machine Learning Devops ND"]

def test_sal_less_50k():
    data = {
        "sno": 6,
        "age": 49,
        "workclass": "Private",
        "education": "9th",
        "education-num": 9,
        "marital-status": "Married-spouse-absent",
        "occupation": "Other-service",
        "relationship": "Not-in-family",
        "race": " Black",
        "sex": "Female",
        "hours-per-week": "16",
        "native-country": "Jamaica"
    } 
    r = client.post("/predict/", json=data)
    assert r.status_code == 200
    assert r.json() == {"salary": "<=50k"}

def test_sal_more_50k():
    data = {
    "sno":1,
    "age": 27, 
    "workclass": "Private", 
    "education": "Bachelors", 
    "marital-status": "Divorced", 
    "occupation": "Adm-clerical", 
    "relationship": "Not-in-family", 
    "race": "White", 
    "sex": "Female", 
    "hours-per-week": 48, 
    "native-country": "United-States"
    }
    r = client.post("/predict/", json=data)
    assert r.status_code == 200
    assert r.json() == {"salary": ">50k"}

    
   
