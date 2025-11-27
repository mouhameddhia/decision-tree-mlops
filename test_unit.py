# tests/test_unit.py
import numpy as np
import pandas as pd
import pytest
from model_pipeline import prepare_data, train_decision_tree, evaluate_model


# Dummy dataset
@pytest.fixture
def dummy_dataset():
    data = {
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Class": [0, 1, 0, 1, 0],
    }
    return pd.DataFrame(data)


def test_prepare_data_shapes(dummy_dataset):
    x_train, x_test, y_train, y_test, scaler = prepare_data(
        dummy_dataset, test_size=0.2
    )
    assert x_train.shape[0] == 4
    assert x_test.shape[0] == 1
    assert len(y_train) == 4
    assert len(y_test) == 1


def test_train_decision_tree_returns_model(dummy_dataset):
    x_train, x_test, y_train, y_test, scaler = prepare_data(dummy_dataset)
    model = train_decision_tree(x_train, y_train)
    assert model is not None
    assert hasattr(model, "predict")


def test_evaluate_model_metrics(dummy_dataset):
    x_train, x_test, y_train, y_test, scaler = prepare_data(dummy_dataset)
    model = train_decision_tree(x_train, y_train)
    metrics, y_pred = evaluate_model(model, x_test, y_test)
    assert "accuracy" in metrics
    assert "confusion_matrix" in metrics
    assert isinstance(y_pred, np.ndarray)
