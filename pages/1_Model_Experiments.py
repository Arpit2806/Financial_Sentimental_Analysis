import streamlit as st

def model_experiments_page():

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.metrics import confusion_matrix, classification_report

    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, LSTM, Dense

    # -----------------------------------------
    # HEADER
    # -----------------------------------------
    st.header("🤖 Model Experiments (LSTM Pipeline)")

    st.markdown("""
    This module demonstrates the **end-to-end NLP pipeline** used in the project:
    - Text preprocessing  
    - Tokenization & padding  
    - LSTM-based model training  
    - Performance evaluation  
    """)

    # -----------------------------------------
    # LOAD DATA
    # -----------------------------------------
    df = pd.read_csv("all-data.csv", encoding="latin-1")
    df.columns = ["sentiment", "text"]

    st.subheader("📊 Dataset Overview")
    st.dataframe(df.head())

    # -----------------------------------------
    # RUN MODEL?
    # -----------------------------------------
    run_model = st.radio(
        "Do you want to run the model pipeline?",
        ["Yes, run model", "No"]
    )

    if run_model != "Yes, run model":
        st.info("Select 'Yes' to execute the model pipeline.")
        return

    # -----------------------------------------
    # LABEL ENCODING
    # -----------------------------------------
    le = LabelEncoder()
    y = le.fit_transform(df["sentiment"])

    # -----------------------------------------
    # TOKENIZATION
    # -----------------------------------------
    st.subheader("🔤 Text Tokenization")

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(df["text"])

    sequences = tokenizer.texts_to_sequences(df["text"])
    X = pad_sequences(sequences, maxlen=50)

    st.success("Text successfully tokenized and padded.")

    # -----------------------------------------
    # TRAIN TEST SPLIT
    # -----------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -----------------------------------------
    # MODEL BUILDING
    # -----------------------------------------
    st.subheader("🧠 Building LSTM Model")

    model = Sequential([
        Embedding(input_dim=5000, output_dim=128, input_length=50),
        LSTM(64),
        Dense(3, activation="softmax")
    ])

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"]
    )

    st.info("Model architecture: Embedding → LSTM → Dense")

    # -----------------------------------------
    # TRAIN MODEL
    # -----------------------------------------
    st.subheader("📈 Training Model")

    history = model.fit(
        X_train,
        y_train,
        epochs=3,   # keep small for speed
        batch_size=32,
        validation_split=0.2,
        verbose=0
    )

    st.success("Model training completed.")

    # -----------------------------------------
    # ACCURACY GRAPH
    # -----------------------------------------
    st.subheader("📊 Training vs Validation Accuracy")

    fig1, ax1 = plt.subplots()
    ax1.plot(history.history["accuracy"], label="Train Accuracy")
    ax1.plot(history.history["val_accuracy"], label="Validation Accuracy")
    ax1.legend()
    st.pyplot(fig1)

    # -----------------------------------------
    # LOSS GRAPH
    # -----------------------------------------
    st.subheader("📉 Training vs Validation Loss")

    fig2, ax2 = plt.subplots()
    ax2.plot(history.history["loss"], label="Train Loss")
    ax2.plot(history.history["val_loss"], label="Validation Loss")
    ax2.legend()
    st.pyplot(fig2)

    # -----------------------------------------
    # EVALUATION
    # -----------------------------------------
    st.subheader("🔍 Model Evaluation")

    y_pred = np.argmax(model.predict(X_test), axis=1)

    cm = confusion_matrix(y_test, y_pred)

    fig3, ax3 = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax3)
    ax3.set_xlabel("Predicted")
    ax3.set_ylabel("Actual")
    st.pyplot(fig3)

    st.subheader("📋 Classification Report")
    report = classification_report(y_test, y_pred, target_names=le.classes_)
    st.text(report)

    # -----------------------------------------
    # FINAL INSIGHT
    # -----------------------------------------
    st.success("🚀 LSTM model successfully captures sentiment patterns in financial text.")
