import requests
import json

data = {
        "age": 34,
        "workclass": "Private",
        "education": "Bachelors",
        "education-num": 9,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Wife",
        "race": " White",
        "sex": "Female",
        "hours-per-week": "55",
        "native-country": " United-States",
    } 

r = requests.post("http://127.0.0.1:8000/predict/", data = json.dumps(data))

print(r.json())

