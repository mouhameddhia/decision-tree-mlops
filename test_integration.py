# tests/test_integration.py
import pandas as pd
import pytest
from model_pipeline import run_complete_pipeline


@pytest.fixture
def temp_csv(tmp_path):
    file_path = tmp_path / "dummy.csv"
    data = {
        "Variance": [2, 3, 1, 5],
        "Skewness": [0.1, -0.2, 0.5, 0.0],
        "Curtosis": [1, 2, 1, 2],
        "Entropy": [0, 1, 0, 1],
        "Class": [0, 1, 0, 1],
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    return file_path


def test_run_complete_pipeline(temp_csv):
    model, metrics, scaler = run_complete_pipeline(temp_csv)

    # Check that model trained
    assert model is not None

    # Check that metrics exist
    assert "accuracy" in metrics

    # Check scaler exists
    assert scaler is not None

    # Check a simple prediction
    sample = [[2, 0.1, 1, 0]]
    pred = model.predict(scaler.transform(sample))
    assert pred.shape[0] == 1
