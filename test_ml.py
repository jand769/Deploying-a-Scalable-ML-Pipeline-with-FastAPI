import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.model import train_model, compute_model_metrics
from ml.data import process_data

# Test 1: Ensure train_model trains a RandomForestClassifier
def test_train_model():
    """
    Ensure that the train_model function trains and returns a RandomForestClassifier.
    """
    X_train = np.random.rand(50, 5)  # Mock training data
    y_train = np.random.randint(0, 2, size=50)  # Mock binary labels
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "train_model did not return a RandomForestClassifier."

# Test 2: Validate that compute_model_metrics returns precision, recall, and F1 as floats
def test_compute_model_metrics():
    """
    Validate that compute_model_metrics returns precision, recall, and F1-score as floats.
    """
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert isinstance(precision, float), "Precision is not a float."
    assert isinstance(recall, float), "Recall is not a float."
    assert isinstance(fbeta, float), "F1-score is not a float."
    assert 0 <= precision <= 1, "Precision is out of range."
    assert 0 <= recall <= 1, "Recall is out of range."
    assert 0 <= fbeta <= 1, "F1-score is out of range."

# Test 3: Ensure train-test split size is correct (80% train, 20% test)
def test_train_test_split_size():
    """
    Ensure that the train-test split results in datasets of the expected size (80% train, 20% test).
    """
    data = np.random.rand(100, 5)  # Mock dataset with 100 samples, 5 features
    labels = np.random.randint(0, 2, size=100)  # Mock binary labels
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    assert len(X_train) == 80, "Train dataset size is incorrect."
    assert len(X_test) == 20, "Test dataset size is incorrect."
    assert len(y_train) == 80, "Train labels size is incorrect."
    assert len(y_test) == 20, "Test labels size is incorrect."
