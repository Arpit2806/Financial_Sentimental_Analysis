import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide"
)

# -------------------------------
# 🎨 CLASSY DARK FINTECH THEME
# -------------------------------
st.markdown("""
<style>

/* ---- GLOBAL BACKGROUND ---- */
body {
    background-color: #0f172a;
}

/* ---- MAIN CONTENT AREA ---- */
.block-container {
    padding-top: 2rem;
    background-color: #111827;
    border-radius: 12px;
    padding: 2rem;
}

/* ---- SIDEBAR ---- */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

/* ---- HEADINGS ---- */
h1 {
    color: #f8fafc;
    font-weight: 600;
}

h2, h3 {
    color: #e2e8f0;
}

/* ---- TEXT ---- */
p, li {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.6;
}

/* ---- DIVIDER ---- */
hr {
    border: 0.5px solid #334155;
}

/* ---- FOOTER ---- */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #020617;
    color: #94a3b8;
    text-align: center;
    padding: 12px;
    font-size: 13px;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 HOME PAGE CONTENT
# -------------------------------
st.title("🏠 About Capstone")

st.markdown("### Financial Analytics Dashboard")

st.markdown("""
## 💡 AI-Driven Financial Sentiment Intelligence

---

### 📌 Overview
A system designed to extract **actionable insights from financial news** using advanced NLP and deep learning techniques.

---

### ⚙️ Core Modules

**Model Analysis**
- Baseline LSTM  
- BiLSTM with Attention  
- Captures contextual dependencies in financial text  

**Sentiment Engine**
- VADER (rule-based baseline)  
- FinBERT (financial domain model)  
- Comparative evaluation of sentiment accuracy  

**Prediction Interface**
- Upload financial datasets  
- Analyze sentiment distribution  
- Generate quick predictions  

---

### 📊 Capabilities

- Sentiment classification (Positive / Neutral / Negative)  
- Model performance comparison  
- Interactive visualizations  
- Dataset-driven insights  

---

### 🎯 Application Value

- Faster interpretation of financial news  
- Identification of sentiment-driven trends  
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
# 📌 FIXED FOOTER
# -------------------------------
st.markdown(
    '<div class="footer">FINAL CAPSTONE PROJECT</div>',
    unsafe_allow_html=True
)
