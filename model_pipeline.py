# model_pipeline.py
"""
Modular Machine Learning Pipeline for Decision Tree Classification
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn import tree
import joblib
import os


def load_data(file_path):
    """
    Load the dataset from CSV file
    
    Parameters:
    -----------
    file_path : str
        Path to the CSV data file
    
    Returns:
    --------
    pandas.DataFrame : Loaded dataset
    """
    print(f"📁 Loading data from {file_path}...")
    dataset = pd.read_csv(file_path)
    print(f"✅ Dataset loaded successfully! Shape: {dataset.shape}")
    return dataset


def explore_data(dataset):
    """
    Perform exploratory data analysis
    
    Parameters:
    -----------
    dataset : pandas.DataFrame
        The dataset to explore
    """
    print("\n🔍 Exploring Data...")
    print(f"Dataset shape: {dataset.shape}")
    print("\nFirst 5 rows:")
    print(dataset.head())
    print("\nLast 5 rows:")
    print(dataset.tail())
    print("\nDataset info:")
    print(dataset.info())
    print("\nStatistical summary:")
    print(dataset.describe())
    print("\nClass distribution:")
    print(dataset['Class'].value_counts())


def prepare_data(dataset, test_size=0.2, random_state=0):
    """
    Prepare data for training by splitting and scaling
    
    Parameters:
    -----------
    dataset : pandas.DataFrame
        The dataset to prepare
    test_size : float, default=0.2
        Proportion of dataset for testing
    random_state : int, default=0
        Random state for reproducibility
    
    Returns:
    --------
    tuple : (X_train, X_test, y_train, y_test, scaler)
        Prepared training and testing data with fitted scaler
    """
    print("🔧 Preparing data for training...")
    
    # Prepare input features and target
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Feature scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    print("✅ Data preparation completed!")
    print(f"Training set shape: {X_train.shape}")
    print(f"Test set shape: {X_test.shape}")
    
    return X_train, X_test, y_train, y_test, scaler


def train_decision_tree(X_train, y_train, criterion='entropy', random_state=0):
    """
    Train a Decision Tree Classifier
    
    Parameters:
    -----------
    X_train : array-like
        Training features
    y_train : array-like
        Training labels
    criterion : str, default='entropy'
        Splitting criterion ('gini' or 'entropy')
    random_state : int, default=0
        Random state for reproducibility
    
    Returns:
    --------
    DecisionTreeClassifier : Trained model
    """
    print("🤖 Training Decision Tree Classifier...")
    
    # Initialize and train the model
    classifier = DecisionTreeClassifier(criterion=criterion, random_state=random_state)
    classifier.fit(X_train, y_train)
    
    print("✅ Model training completed!")
    
    return classifier


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model performance
    
    Parameters:
    -----------
    model : trained classifier
        The trained Decision Tree model
    X_test : array-like
        Test features
    y_test : array-like
        True test labels
    
    Returns:
    --------
    tuple : (metrics_dict, y_pred)
        Evaluation metrics and predictions
    """
    print("📊 Evaluating model performance...")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred) * 100
    report = classification_report(y_test, y_pred)
    
    # Print results
    print("Confusion Matrix:")
    print(cm)
    print(f"\nAccuracy: {accuracy:.2f}%")
    print("\nClassification Report:")
    print(report)
    
    # Return metrics as dictionary
    metrics = {
        'confusion_matrix': cm,
        'accuracy': accuracy,
        'classification_report': report
    }
    
    return metrics, y_pred


def save_model(model, file_path='decision_tree_model.joblib'):
    """
    Save the trained model
    
    Parameters:
    -----------
    model : trained classifier
        The trained Decision Tree model
    file_path : str, default='decision_tree_model.joblib'
        Path to save the model
    """
    joblib.dump(model, file_path)
    print(f"💾 Model saved successfully to {file_path}")


def load_model(file_path='decision_tree_model.joblib'):
    """
    Load a saved model
    
    Parameters:
    -----------
    file_path : str, default='decision_tree_model.joblib'
        Path to the saved model file
    
    Returns:
    --------
    trained classifier : Loaded model
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Model file {file_path} not found!")
    
    model = joblib.load(file_path)
    print(f"📂 Model loaded successfully from {file_path}")
    
    return model


def visualize_tree(model, feature_names=None, class_names=None, save_path='decision_tree_structure.txt'):
    """
    Visualize the decision tree (text representation)
    
    Parameters:
    -----------
    model : trained DecisionTreeClassifier
        The trained decision tree model
    feature_names : list, optional
        Names of the features
    class_names : list, optional
        Names of the classes
    save_path : str, optional
        Path to save the text representation
    """
    print("🌳 Generating decision tree visualization...")
    
    # Generate text representation
    text_representation = tree.export_text(
        model, 
        feature_names=feature_names,
        class_names=class_names
    )
    
    print("Decision Tree Text Representation:")
    print(text_representation)
    
    # Save to file if path provided
    if save_path:
        with open(save_path, 'w') as f:
            f.write(text_representation)
        print(f"💾 Tree representation saved to {save_path}")
    
    return text_representation


def run_complete_pipeline(data_path, test_size=0.2, random_state=0, criterion='entropy'):
    """
    Run the complete ML pipeline from data loading to evaluation
    
    Parameters:
    -----------
    data_path : str
        Path to the dataset CSV file
    test_size : float, default=0.2
        Proportion of dataset for testing
    random_state : int, default=0
        Random state for reproducibility
    criterion : str, default='entropy'
        Splitting criterion for Decision Tree
    
    Returns:
    --------
    tuple : (model, metrics, scaler)
        Trained model, evaluation metrics, and fitted scaler
    """
    print("🚀 Starting Complete Pipeline...")
    
    # Step 1: Load data
    dataset = load_data(data_path)
    
    # Step 2: Explore data
    explore_data(dataset)
    
    # Step 3: Prepare data
    X_train, X_test, y_train, y_test, scaler = prepare_data(
        dataset, test_size=test_size, random_state=random_state
    )
    
    # Step 4: Train model
    model = train_decision_tree(
        X_train, y_train, 
        criterion=criterion, 
        random_state=random_state
    )
    
    # Step 5: Evaluate model
    metrics, y_pred = evaluate_model(model, X_test, y_test)
    
    # Step 6: Save model
    save_model(model)
    
    # Step 7: Visualize tree
    feature_names = ['Variance', 'Skewness', 'Curtosis', 'Entropy']
    class_names = ['Authentic', 'Forged']
    visualize_tree(model, feature_names, class_names)
    
    print("✅ Complete pipeline finished successfully!")
    
    return model, metrics, scaler