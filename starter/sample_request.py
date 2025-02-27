import requests
import json

data = {
        "sno": 1,
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

r = requests.get("https://mldevops-project3.onrender.com/")
print(r.json())
print("\n")

print(data)
print("\n")
r = requests.post("https://mldevops-project3.onrender.com/predict", data = json.dumps(data))

print("prediction")
print(r.json())
