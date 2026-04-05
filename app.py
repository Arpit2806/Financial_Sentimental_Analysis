import streamlit as st

st.set_page_config(
    page_title="AI Financial Dashboard",
    layout="wide"
)

# ---- SIDEBAR ----
st.sidebar.title("📊 Navigation")
st.sidebar.info("""
Select a module:

1️⃣ Model Experiments  
2️⃣ Sentiment Comparison  
""")

# ---- HOME PAGE ----
st.title("💡 AI-Driven Financial News Sentiment Analysis")

st.markdown("""
### 🎯 What This Project Does
- Analyze financial news using NLP  
- Compare sentiment models  
- Predict market movement  

---

### ❓ Why This Matters
Financial markets react instantly to news sentiment.  
This project helps:
- Understand sentiment trends  
- Evaluate AI models  
- Support better investment decisions  

---

### 🔁 Project Flow

➡️ Step 1: Model Experiments (ML models from v7.ipynb)  
➡️ Step 2: Sentiment Comparison (VADER vs FinBERT)  

---

### 📊 What You Will See in Dashboard

- Model performance comparisons  
- Graphs & visualizations from notebooks  
- Sentiment analysis insights  

---

### 🧠 MBA Angle
This dashboard acts as a **Decision Support System**  
for investors using AI + NLP.
""")
