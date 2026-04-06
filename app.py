import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide"
)

# -------------------------------
# 🎨 CLEAN LIGHT FINTECH STYLE
# -------------------------------
st.markdown("""
<style>

/* Better spacing */
.block-container {
    padding-top: 2rem;
}

/* Headings */
h1 {
    font-weight: 700;
}

h2, h3 {
    margin-top: 1rem;
}

/* Subtle divider */
hr {
    border: 0.5px solid #e5e7eb;
}

/* Footer */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f9fafb;
    color: #6b7280;
    text-align: center;
    padding: 10px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 HOME PAGE
# -------------------------------
st.title("🏠 About Capstone")

st.markdown("### Financial Analytics Dashboard")

st.markdown("""
## 💡 AI-Driven Financial Sentiment Intelligence

---

### 📌 Overview
A system designed to extract **actionable insights from financial news** using NLP and deep learning models.

---

### ⚙️ Core Modules

**Model Analysis**
- Baseline LSTM  
- BiLSTM with Attention  
- Captures contextual relationships in financial text  

**Sentiment Engine**
- VADER (rule-based)  
- FinBERT (financial-domain model)  
- Comparative performance evaluation  

**Prediction Interface**
- Upload datasets  
- Analyze sentiment  
- Generate predictions  

---

### 📊 Capabilities

- Sentiment classification (Positive / Neutral / Negative)  
- Model comparison  
- Interactive visualizations  
- Dataset-driven insights  

---

### 🎯 Business Value

- Faster interpretation of financial news  
- Identification of sentiment-driven trends  
- Better decision support  

---

### 🔁 Workflow

1. Data ingestion  
2. Preprocessing  
3. Model analysis  
4. Sentiment evaluation  
5. Visualization  

""")

# -------------------------------
# 📌 FOOTER
# -------------------------------
st.markdown(
    '<div class="footer">FINAL CAPSTONE PROJECT</div>',
    unsafe_allow_html=True
)
