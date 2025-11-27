# model_pipeline.py
"""
Modular Machine Learning Pipeline for Decision Tree Classification
"""

# ------------------------
# Standard library imports
# ------------------------
import os

# ------------------------
# Third-party imports
# ------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import joblib
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ------------------------
# Local imports
# ------------------------
from plot_metrics import save_accuracy_plot


# ------------------------
# Pipeline functions
# ------------------------


def load_data(file_path):
    """Load dataset from CSV file."""
    print(f"📁 Loading data from {file_path}...")
    dataset = pd.read_csv(file_path)
    print(f"✅ Dataset loaded successfully! Shape: {dataset.shape}")
    return dataset


def explore_data(dataset):
    """Perform exploratory data analysis."""
    print("\n🔍 Exploring Data...")
    print(f"Dataset shape: {dataset.shape}")
    print("\nFirst 5 rows:\n", dataset.head())
    print("\nLast 5 rows:\n", dataset.tail())
    print("\nDataset info:")
    print(dataset.info())
    print("\nStatistical summary:")
    print(dataset.describe())
    print("\nClass distribution:")
    print(dataset["Class"].value_counts())


def prepare_data(dataset, test_size=0.2, random_state=0):
    """Prepare data for training by splitting and scaling."""
    print("🔧 Preparing data for training...")

    x_features = dataset.iloc[:, :-1].values
    y_labels = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(
        x_features, y_labels, test_size=test_size, random_state=random_state
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    print("✅ Data preparation completed!")
    print(f"Training set shape: {x_train.shape}")
    print(f"Test set shape: {x_test.shape}")

    return x_train, x_test, y_train, y_test, scaler


def train_decision_tree(x_train, y_train, criterion="entropy", random_state=0):
    """Train a Decision Tree Classifier."""
    print("🤖 Training Decision Tree Classifier...")

    classifier = DecisionTreeClassifier(criterion=criterion, random_state=random_state)
    classifier.fit(x_train, y_train)

    print("✅ Model training completed!")
    return classifier


def evaluate_model(model, x_test, y_test):
    """Evaluate trained model performance."""
    print("📊 Evaluating model performance...")

    y_pred = model.predict(x_test)

    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred) * 100
    report = classification_report(y_test, y_pred)

    print("Confusion Matrix:\n", cm)
    print(f"\nAccuracy: {accuracy:.2f}%")
    print("\nClassification Report:\n", report)

    save_accuracy_plot(accuracy)

    metrics = {
        "confusion_matrix": cm,
        "accuracy": accuracy,
        "classification_report": report,
    }

    return metrics, y_pred


def save_model(model, file_path="decision_tree_model.joblib"):
    """Save the trained model."""
    joblib.dump(model, file_path)
    print(f"💾 Model saved successfully to {file_path}")


def load_model(file_path="decision_tree_model.joblib"):
    """Load a saved model."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Model file {file_path} not found!")

    model = joblib.load(file_path)
    print(f"📂 Model loaded successfully from {file_path}")
    return model


def visualize_tree(
    model, feature_names=None, class_names=None, save_path="decision_tree_structure.txt"
):
    """Visualize the decision tree (text representation)."""
    print("🌳 Generating decision tree visualization...")

    text_representation = export_text(
        model, feature_names=feature_names, show_weights=False
    )

    print("Decision Tree Text Representation:\n", text_representation)

    if save_path:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text_representation)
        print(f"💾 Tree representation saved to {save_path}")

    return text_representation


def generate_pdf_report(metrics, save_path="reports/pipeline_report.pdf"):
    """Generate PDF report with model evaluation metrics."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    c = canvas.Canvas(save_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Decision Tree Pipeline Report")

    c.setFont("Helvetica", 12)
    y = height - 100

    accuracy = metrics.get("accuracy", "N/A")
    c.drawString(50, y, f"Accuracy: {accuracy:.2f}%")
    y -= 30

    cm = metrics.get("confusion_matrix")
    if cm is not None:
        c.drawString(50, y, "Confusion Matrix:")
        y -= 20
        for row in cm:
            c.drawString(70, y, "  ".join(str(x) for x in row))
            y -= 20

    report = metrics.get("classification_report")
    if report:
        y -= 10
        c.drawString(50, y, "Classification Report:")
        y -= 20
        for line in report.split("\n"):
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 50
            c.drawString(50, y, line)
            y -= 15

    c.save()
    print(f"💾 PDF report saved to {save_path}")


def run_complete_pipeline(
    data_path, test_size=0.2, random_state=0, criterion="entropy"
):
    """Run the complete ML pipeline from data loading to evaluation."""
    print("🚀 Starting Complete Pipeline...")

    dataset = load_data(data_path)
    explore_data(dataset)
    x_train, x_test, y_train, y_test, scaler = prepare_data(
        dataset, test_size=test_size, random_state=random_state
    )

    model = train_decision_tree(
        x_train, y_train, criterion=criterion, random_state=random_state
    )
    metrics, _ = evaluate_model(model, x_test, y_test)

    save_model(model)

    feature_names = ["Variance", "Skewness", "Curtosis", "Entropy"]
    class_names = ["Authentic", "Forged"]
    visualize_tree(model, feature_names, class_names)

    generate_pdf_report(metrics)

    print("✅ Complete pipeline finished successfully!")
    return model, metrics, scaler
