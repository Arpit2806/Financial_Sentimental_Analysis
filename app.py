import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide"
)

# -------------------------------
# 🎨 PREMIUM DARK FINTECH STYLE
# -------------------------------
st.markdown("""
<style>
/* Main background */
body {
    background-color: #0e1117;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Titles */
h1, h2, h3 {
    color: #e5e7eb;
}

/* Text */
p, li {
    color: #9ca3af;
}

/* Cards */
.block-container {
    padding-top: 2rem;
}

/* Footer */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #111827;
    color: #9ca3af;
    text-align: center;
    padding: 10px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 HOME TITLE (REPLACES "app")
# -------------------------------
st.title("🏠 About Capstone")

st.markdown("""
## 💡 AI-Driven Financial Sentiment Intelligence

---

### 📌 Overview

This project builds a **financial sentiment intelligence system** that transforms 
unstructured news data into meaningful market insights.

It leverages:
- Deep Learning (LSTM, BiLSTM + Attention)
- NLP techniques for text understanding
- Financial-domain sentiment analysis

---

### ⚙️ System Architecture

**1. Model Layer**
- Baseline LSTM  
- BiLSTM with Attention  
- Captures sequential and contextual patterns  

**2. Sentiment Layer**
- VADER (rule-based baseline)  
- FinBERT (domain-specific model)  
- Comparative evaluation  

**3. Application Layer**
- Interactive dashboard  
- Dataset ingestion  
- Real-time sentiment exploration  

---

### 📊 Key Capabilities

- Sentiment classification (Positive / Neutral / Negative)  
- Model comparison and evaluation  
- Visualization of sentiment distribution  
- Interactive dataset analysis  

---

### 🎯 Practical Value

- Faster interpretation of financial news  
- Identification of sentiment-driven signals  
- Improved analytical decision-making  

---

### 🔁 Workflow

1. Data ingestion  
2. Preprocessing  
3. Model-based classification  
4. Comparative evaluation  
5. Visualization & insights  

""")

# -------------------------------
# 📌 FOOTER (FIXED)
# -------------------------------
st.markdown(
    '<div class="footer">FINAL CAPSTONE PROJECT</div>',
    unsafe_allow_html=True
)
