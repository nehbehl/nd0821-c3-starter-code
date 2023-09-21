# Model Card


A machine learning model using the RandomForestClassifier from the scikit-learn library and it models the US census data.


## Model Details
 The model is trained using the train_model function, which takes in the training data (X_train) and labels (y_train) as inputs. Inside the train_model function, the SMOTE (Synthetic Minority Over-sampling Technique) algorithm is used to handle class imbalance by oversampling the minority class. The oversampled data is then used to train the RandomForestClassifier model.

The compute_model_metrics function is used to evaluate the performance of the trained model. It takes in the known labels (y) and the predicted labels (preds) as inputs and computes precision, recall, and F1 score using the precision_score, recall_score, and fbeta_score functions from the scikit-learn library.

The inference function takes a trained machine learning model (model) and new data (X) as inputs and returns the predictions made by the model.

## Intended Use
This has been created to evaluate Deploying a Scalable ML Pipeline in Production project.

## Training Data

This model is trained on US Census Income Data Set from https://archive.ics.uci.edu/ml/datasets/census+income
It has been cleaned for invalid records.

## Evaluation Data
This has been performed with the Census Income Data Set.

## Metrics
Calculates precision, recall and fbeta for metrics.

## Ethical Considerations

## Caveats and Recommendations
