# Script to train machine learning model.
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sys
from pathlib import Path

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

precision, recall, fbeta = compute_model_metrics(y_test, predictions)

print(precision,recall,fbeta)

## Unit tests 
def test_train_model():
    assert isinstance(model, RandomForestClassifier)
    print("Passed train model check")

def test_inference():
    assert isinstance(predictions, np.ndarray)
    print("Passed inference check")

def test_metrics():
    assert math.isclose(precision, 0.6, rel_tol=1), "precision should be close to 0.63"
    print("Passed metrics check")

print("Running unit tests")
test_train_model()
test_inference()
test_metrics()




