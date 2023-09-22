import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_data_success():
    data = {"feature_1": 1, "feature_2": "test string"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 200


def test_post_data_fail():
    data = {"feature_1": -5, "feature_2": "test string"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 400

def test_get():
    """
    Test welcome message for get at root
    """
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == "Hello to Udacity Machine Learning Devops ND"


def test_ingest_data1():
    sample =  {  'age':50,
                'workclass':"Private", 
                'education':"Doctorate",
                'marital_status':"Separated",
                'occupation':"Exec-managerial",
                'relationship':"Not-in-family",
                'race':"Black",
                'sex':"Female",
                'hours_per_week':50,
                'native_country':"United-States"
            }

    data = json.dumps(sample)

    r = client.post("/data/", data=data )

    assert r.status_code == 200
    assert r.json()["hours_per_week"] == 50
    assert r.json()["sex"] == "Female"

    assert r.json()["prediction"] == '>50K'


def test_ingest_data2():
    sample =  {  'age':30,
                'workclass':"Private", 
                'education':"HS-grad",
                'marital_status':"Separated",
                'occupation':"Handlers-cleaners",
                'relationship':"Not-in-family",
                'race':"Black",
                'sex':"Male",
                'hours_per_week':35,
                'native_country':"United-States"
            }

    data = json.dumps(sample)

    r = client.post("/data/", data=data )

    # test response and output
    assert r.status_code == 200
    assert r.json()["age"] == 30
    
    assert r.json()["prediction"][0] == '<=50K'
