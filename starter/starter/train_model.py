# Script to train machine learning model.
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Add the necessary imports for the starter code.
import pandas as pd
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference
import numpy as np
import math

### Clean data
df = pd.read_csv('../data/census.csv')

df.columns = df.columns.str.strip()
       
df['salary'] = df['salary'].str.lstrip()
df.drop("capital-gain", axis="columns", inplace=True)
df.drop("capital-loss", axis="columns", inplace=True)
df.drop("fnlgt", axis="columns", inplace=True)
df.drop("education-num", axis="columns", inplace=True)
       
df.to_csv('clean_census.csv')

### Slice data
def slicing(data):
    sliced = []

    for category in cat_features:
        for cls in test[category].unique():
            df_temp = test[test[category] == cls]
            X_test_temp, y_test_temp, _, _ = process_data(
                df_temp, categorical_features=cat_features,
                label="salary", encoder=encoder, lb=lb, training=False)
            y_preds = model.predict(X_test_temp)
            precision_temp, recall_temp, fbeta_temp = compute_model_metrics(
                y_test_temp, y_preds)
            results = "[%s->%s] Precision: %s " \
                "Recall: %s FBeta: %s" % (
                    category,
                    cls,
                    precision_temp,
                    recall_temp,
                    fbeta_temp)
            sliced.append(results)

    with open('slice_output.txt', 'w') as out:
        for slice in sliced:
            out.write(slice + '\n')



# Add code to load in the data.
data = pd.read_csv('clean_census.csv')


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

print(X_train)
# Train and save a model.
model = train_model(X_train, y_train)
predictions = inference(model, X_test)

precision, recall, fbeta = compute_model_metrics(y_test, predictions)

slicing(data)

## Unit tests 
def test_train_model():
    assert isinstance(model, RandomForestClassifier)

def test_inference():
    assert isinstance(predictions, np.ndarray)

def test_metrics():
    assert math.isclose(precision, 0.6, rel_tol=1), "precision should be close to 0.63"


test_train_model()
test_inference()
test_metrics()




