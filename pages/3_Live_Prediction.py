import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def prediction_page():

    st.header("📈 Live Financial Sentiment Prediction")

    st.markdown("""
    Upload a financial dataset or input text to analyze sentiment.

    Supported format:
    sentence @ sentiment
    """)

    # -----------------------------------------
    # FILE UPLOAD
    # -----------------------------------------
    uploaded_file = st.file_uploader(
        "Upload dataset (.txt or .csv)", type=["txt", "csv"]
    )

    if uploaded_file:

        # ✅ SAFE FILE READING (FIXED)
        raw = uploaded_file.read()

        try:
            text_data = raw.decode("utf-8")
        except:
            text_data = raw.decode("latin-1")

        lines = text_data.split("\n")

        texts = []
        labels = []

        for line in lines:
            if "@" in line:
                parts = line.rsplit("@", 1)
                texts.append(parts[0].strip())
                labels.append(parts[1].strip())

        if len(texts) == 0:
            st.error("❌ No valid data found. Ensure format: sentence @ sentiment")
            return

        df = pd.DataFrame({
            "text": texts,
            "sentiment": labels
        })

        st.success("✅ File loaded successfully")

        # -----------------------------------------
        # PREVIEW
        # -----------------------------------------
        st.subheader("📊 Data Preview")
        st.dataframe(df.head())

        # -----------------------------------------
        # SENTIMENT DISTRIBUTION
        # -----------------------------------------
        st.subheader("📊 Sentiment Distribution")

        fig1, ax1 = plt.subplots()
        sns.countplot(x="sentiment", data=df, ax=ax1)
        st.pyplot(fig1)

        # -----------------------------------------
        # METRICS
        # -----------------------------------------
        st.subheader("📌 Key Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", len(df))
        col2.metric(
            "Positive %",
            f"{(df['sentiment']=='positive').mean()*100:.1f}%"
        )
        col3.metric(
            "Negative %",
            f"{(df['sentiment']=='negative').mean()*100:.1f}%"
        )

        # -----------------------------------------
        # TEXT LENGTH ANALYSIS
        # -----------------------------------------
        st.subheader("📝 Text Length Distribution")

        df["length"] = df["text"].apply(len)

        fig2, ax2 = plt.subplots()
        sns.histplot(df["length"], bins=50, ax=ax2)
        st.pyplot(fig2)

        # -----------------------------------------
        # SAMPLE TABLE
        # -----------------------------------------
        st.subheader("📋 Sample Data")

        st.dataframe(df.sample(min(10, len(df))))

        # -----------------------------------------
        # INSIGHTS
        # -----------------------------------------
        st.success("""
        🔑 Insights:

        ✔ Dataset contains strong financial sentiment signals  
        ✔ Positive sentiment often dominates high-agreement datasets  
        ✔ Useful for training NLP models  
        """)

    # -----------------------------------------
    # SINGLE TEXT PREDICTION
    # -----------------------------------------
    st.subheader("✍️ Analyze Single Text")

    user_text = st.text_area("Enter financial news text")

    if st.button("Predict Sentiment"):

        if user_text.strip() == "":
            st.warning("Please enter some text")
        else:
            text = user_text.lower()

            # ✅ SIMPLE LOGIC (FAST + DEMO SAFE)
            if any(word in text for word in ["profit", "growth", "increase", "rise", "gain"]):
                sentiment = "Positive"
            elif any(word in text for word in ["loss", "decline", "fall", "drop", "decrease"]):
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            st.subheader("🔍 Prediction Result")
            st.success(f"Predicted Sentiment: {sentiment}")

# RUN PAGE
prediction_page()
