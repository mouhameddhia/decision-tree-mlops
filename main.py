#!/usr/bin/env python3
"""
Main script for Decision Tree Classification Pipeline
Execute the complete pipeline or individual steps
"""
#webhook!!!!
from model_pipeline import *
import argparse
import joblib

def main():
    parser = argparse.ArgumentParser(description='Decision Tree Classification Pipeline')
    parser.add_argument('--prepare', action='store_true', help='Only prepare data')
    parser.add_argument('--train', action='store_true', help='Only train model')
    parser.add_argument('--evaluate', action='store_true', help='Only evaluate model')
    parser.add_argument('--visualize', action='store_true', help='Only visualize tree')
    parser.add_argument('--all', action='store_true', help='Run complete pipeline (default)')
    parser.add_argument('--data_path', type=str, default='bill_authentication.csv', 
                       help='Path to the dataset CSV file')
    
    args = parser.parse_args()
    
    # If no arguments provided, run everything
    if not any([args.prepare, args.train, args.evaluate, args.visualize, args.all]):
        args.all = True
    
    print("🚀 Starting Decision Tree Classification Pipeline...")
    
    if args.prepare or args.all:
        print("\n📁 STEP 1: Preparing Data...")
        # Step 1: Load data
        df = load_data(args.data_path)
        
        # Step 2: Explore data
        explore_data(df)
        
        # Step 3: Prepare data
        X_train, X_test, y_train, y_test, scaler = prepare_data(df)
        
        # Save prepared data for later use
        joblib.dump({
            'X_train': X_train, 
            'X_test': X_test, 
            'y_train': y_train, 
            'y_test': y_test, 
            'scaler': scaler
        }, 'prepared_data.joblib')
        print("✅ Data preparation completed and saved!")
    
    if args.train or args.all:
        print("\n🤖 STEP 2: Training Model...")
        # Load prepared data
        try:
            data = joblib.load('prepared_data.joblib')
            X_train = data['X_train']
            y_train = data['y_train']
        except Exception as e:
            print(f"❌ No prepared data found. Please run --prepare first. Error: {e}")
            return
        
        # Train Decision Tree model
        model = train_decision_tree(X_train, y_train)
        
        # Save the model
        save_model(model, 'decision_tree_model.joblib')
        print("✅ Model training completed!")
    
    if args.evaluate or args.all:
        print("\n📊 STEP 3: Evaluating Model...")
        # Load model and data
        try:
            model = load_model('decision_tree_model.joblib')
            data = joblib.load('prepared_data.joblib')
            X_test = data['X_test']
            y_test = data['y_test']
        except Exception as e:
            print(f"❌ Model or data not found. Please run --train first. Error: {e}")
            return
        
        # Evaluate model
        metrics, y_pred = evaluate_model(model, X_test, y_test)
        
        print("✅ Model evaluation completed!")
    
    if args.visualize or args.all:
        print("\n🌳 STEP 4: Visualizing Decision Tree...")
        # Load model
        try:
            model = load_model('decision_tree_model.joblib')
        except Exception as e:
            print(f"❌ Model not found. Please run --train first. Error: {e}")
            return
        
        # Visualize tree
        feature_names = ['Variance', 'Skewness', 'Curtosis', 'Entropy']
        class_names = ['Authentic', 'Forged']
        tree_text = visualize_tree(model, feature_names, class_names)
        
        print("✅ Tree visualization completed!")
    
    print("\n🎯 Pipeline completed successfully!")

if __name__ == "__main__":
    main()
