import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model_pipeline import (
    load_model,
    prepare_data,
    evaluate_model,
    visualize_tree,
    train_decision_tree,
    save_model,
)

st.title("💻 Decision Tree ML Pipeline Demo")

# Upload CSV
uploaded_file = st.file_uploader("Upload your dataset CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df.head())

    # Prepare data
    X_train, X_test, y_train, y_test, scaler = prepare_data(df)

    # Train model
    if st.button("Train Decision Tree"):
        model = (
            load_model("decision_tree_model.joblib")
            if st.checkbox("Load existing model")
            else None
        )
        if not model:
            model = train_decision_tree(X_train, y_train)
            save_model(model)
        st.success("Model trained successfully!")

        # Feature importance
        st.subheader("Feature Importance")
        feature_names = df.columns[:-1]
        fig, ax = plt.subplots()
        ax.bar(feature_names, model.feature_importances_)
        st.pyplot(fig)

        # Evaluate model
        metrics, y_pred = evaluate_model(model, X_test, y_test)

        # Confusion matrix heatmap
        st.subheader("Confusion Matrix")
        cm = metrics["confusion_matrix"]
        fig2, ax2 = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax2)
        st.pyplot(fig2)

        # Visualize tree (text)
        st.subheader("Decision Tree Structure")
        tree_text = visualize_tree(
            model, feature_names=feature_names, class_names=["Authentic", "Forged"]
        )
        st.text(tree_text)

    # Make predictions
    st.subheader("Predict New Sample")
    sample_input = []
    for col in df.columns[:-1]:
        val = st.number_input(f"Enter {col} value", value=0.0)
        sample_input.append(val)

    if st.button("Predict"):
        model = load_model("decision_tree_model.joblib")
        pred = model.predict([sample_input])
        st.write(f"Prediction: **{pred[0]}**")
