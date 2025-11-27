from model_pipeline import prepare_data, train_decision_tree, evaluate_model
import pandas as pd


def test_full_pipeline_functional():
    # Simulate real user workflow
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Class": [0, 1, 0, 1, 0],
    })

    # FULL PIPELINE
    x_train, x_test, y_train, y_test, scaler = prepare_data(data)
    model = train_decision_tree(x_train, y_train)
    metrics, y_pred = evaluate_model(model, x_test, y_test)

    # EXPECTED USER-LEVEL BEHAVIOR
    assert "accuracy" in metrics
    assert metrics["accuracy"] >= 0.0
    assert len(y_pred) == len(y_test)
