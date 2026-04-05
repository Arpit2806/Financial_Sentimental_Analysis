import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🤖 Model Experiments & Performance")

@st.cache_data
def load_data():
    return pd.read_csv("data/all-data.csv")

df = load_data()

# ---- DATA PREVIEW ----
st.subheader("📊 Dataset Overview")
st.dataframe(df.head())

# ---- SENTIMENT DISTRIBUTION ----
st.subheader("📈 Sentiment Distribution")

fig1 = px.histogram(df, x="sentiment", color="sentiment")
st.plotly_chart(fig1, use_container_width=True)

# ---- TEXT LENGTH ANALYSIS ----
st.subheader("📝 Text Length Analysis")

df["text_length"] = df["text"].apply(len)

fig2 = px.histogram(df, x="text_length", nbins=50)
st.plotly_chart(fig2, use_container_width=True)

# ---- MODEL PERFORMANCE (FROM YOUR V7 LOGIC) ----
st.subheader("⚙️ Model Performance Comparison")

# Replace with your actual results from notebook
models = ["Logistic Regression", "Random Forest", "XGBoost"]
accuracy = [0.78, 0.85, 0.88]

fig3 = px.bar(x=models, y=accuracy, color=models)
st.plotly_chart(fig3, use_container_width=True)

# ---- INSIGHT BOX ----
st.info("📌 XGBoost shows highest accuracy in predicting sentiment-driven market movement.")
