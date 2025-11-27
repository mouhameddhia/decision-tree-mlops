#!/usr/bin/env python3
"""
Main script for Decision Tree Classification Pipeline
Execute the complete pipeline or individual steps
"""
import argparse
import joblib
import os
from model_pipeline import (
    load_data,
    explore_data,
    prepare_data,
    train_decision_tree,
    evaluate_model,
    save_model,
    load_model,
    visualize_tree,
    generate_pdf_report,
)


def prepare_step(data_path):
    """Prepare data and save to disk."""
    print("\n📁 STEP 1: Preparing Data...")
    df = load_data(data_path)
    explore_data(df)
    X_train, X_test, y_train, y_test, scaler = prepare_data(df)
    joblib.dump(
        {
            "X_train": X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test,
            "scaler": scaler,
        },
        "prepared_data.joblib",
    )
    print("✅ Data preparation completed and saved!")
    return X_train, X_test, y_train, y_test


def train_step():
    """Train the model and save it."""
    print("\n🤖 STEP 2: Training Model...")
    try:
        data = joblib.load("prepared_data.joblib")
        X_train, y_train = data["X_train"], data["y_train"]
    except Exception as e:
        print(f"❌ No prepared data found. Please run --prepare first. Error: {e}")
        return None

    model = train_decision_tree(X_train, y_train)
    save_model(model, "decision_tree_model.joblib")
    print("✅ Model training completed!")
    return model


def evaluate_step():
    """Evaluate the trained model and generate PDF report."""
    print("\n📊 STEP 3: Evaluating Model...")
    try:
        model = load_model("decision_tree_model.joblib")
        data = joblib.load("prepared_data.joblib")
        X_test, y_test = data["X_test"], data["y_test"]
    except Exception as e:
        print(f"❌ Model or data not found. Please run --train first. Error: {e}")
        return None

    metrics, _ = evaluate_model(model, X_test, y_test)
    print("✅ Model evaluation completed!")

    # Generate PDF
    try:
        os.makedirs("reports", exist_ok=True)
        generate_pdf_report(metrics, save_path="reports/pipeline_report.pdf")
        print("📄 PDF report generated in 'reports/pipeline_report.pdf'")
    except Exception as e:
        print(f"❌ Could not generate PDF report. Error: {e}")
    return metrics


def visualize_step():
    """Visualize the decision tree."""
    print("\n🌳 STEP 4: Visualizing Decision Tree...")
    try:
        model = load_model("decision_tree_model.joblib")
    except Exception as e:
        print(f"❌ Model not found. Please run --train first. Error: {e}")
        return

    feature_names = ["Variance", "Skewness", "Curtosis", "Entropy"]
    class_names = ["Authentic", "Forged"]
    visualize_tree(model, feature_names, class_names)
    print("✅ Tree visualization completed!")


def main():
    parser = argparse.ArgumentParser(
        description="Decision Tree Classification Pipeline"
    )
    parser.add_argument("--prepare", action="store_true", help="Only prepare data")
    parser.add_argument("--train", action="store_true", help="Only train model")
    parser.add_argument("--evaluate", action="store_true", help="Only evaluate model")
    parser.add_argument("--visualize", action="store_true", help="Only visualize tree")
    parser.add_argument(
        "--all", action="store_true", help="Run complete pipeline (default)"
    )
    parser.add_argument(
        "--data_path",
        type=str,
        default="bill_authentication.csv",
        help="Path to the dataset CSV file",
    )
    args = parser.parse_args()

    # Default to run everything if no arguments are provided
    if not any([args.prepare, args.train, args.evaluate, args.visualize, args.all]):
        args.all = True

    print("🚀 Starting Decision Tree Classification Pipeline...")

    if args.prepare or args.all:
        prepare_step(args.data_path)

    if args.train or args.all:
        train_step()

    if args.evaluate or args.all:
        evaluate_step()

    if args.visualize or args.all:
        visualize_step()

    print("\n🎯 Pipeline completed successfully!")


if __name__ == "__main__":
    main()
