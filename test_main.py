import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_data_success():
    data = {"age": 10, "workclass": "test string", "relationship" : "null"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 200


def test_post_data_fail():
    data = {"age": 0, "workclass": "test string", "relationship" : "null"}
    r = client.post("/data/", data=json.dumps(data))
    assert r.status_code == 400
