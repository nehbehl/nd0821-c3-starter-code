import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)





def test_post_data_fail():
    data = {"age": 0, "workclass": "test string", "relationship" : "null"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 422

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
        "sno": 7,
        "age": 52,
        "workclass": "Self-emp-not-inc",
        "education": "HS-grad",
        "education-num": 9,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": " White",
        "sex": "Male",
        "hours-per-week": "45",
        "native-country": " United-States"
    } 
    r = client.post("/predict/", json=data)
    assert r.status_code == 200
    assert r.json() == {"salary": "<=50k"}
