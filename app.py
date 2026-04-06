import streamlit as st

st.set_page_config(
    page_title="AI Financial Dashboard",
    layout="wide"
)

# -------------------------------
# CUSTOM SIDEBAR (RENAMED)
# -------------------------------
st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "",
    [
        "About Capstone",
        "Baseline LSTM vs BiLSTM+Attention",
        "VADER vs FinBERT",
        "Live Prediction"
    ]
)

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "About Capstone":

    st.title("💡 AI-Driven Financial Sentiment Intelligence")

    st.markdown("""
    ### 📌 Project Overview

    This project develops a **financial sentiment intelligence system** that analyzes 
    news data to extract meaningful signals for market understanding.

    It combines:
    - Natural Language Processing (NLP)
    - Deep Learning Models
    - Domain-specific sentiment analysis

    to transform unstructured financial text into actionable insights.

    ---

    ### ⚙️ Core Components

    **1. Deep Learning Models**
    - Baseline LSTM  
    - BiLSTM with Attention mechanism  
    - Captures contextual relationships in financial text  

    **2. Sentiment Analysis Engines**
    - VADER (rule-based)  
    - FinBERT (financial domain NLP model)  
    - Comparative evaluation for accuracy and relevance  

    **3. Interactive Prediction System**
    - Real-time sentiment inference  
    - Dataset ingestion and visualization  
    - Lightweight prediction logic for fast analysis  

    ---

    ### 📊 Key Capabilities

    - Sentiment classification (Positive / Neutral / Negative)  
    - Model performance comparison  
    - Visualization of sentiment trends  
    - Dataset-driven insights  
    - Interactive analysis interface  

    ---

    ### 🎯 Business Relevance

    Financial markets are highly sensitive to news sentiment.

    This system enables:
    - Faster interpretation of market signals  
    - Improved decision support  
    - Identification of sentiment-driven trends  
    - Better understanding of financial narratives  

    ---

    ### 🔁 Workflow

    1. Data ingestion and preprocessing  
    2. Model-based sentiment classification  
    3. Comparative analysis of NLP approaches  
    4. Visualization and interpretation  
    5. Real-time user-driven prediction  

    """)

    st.markdown("---")
    st.markdown("### 📌 FINAL CAPSTONE PROJECT")

# -------------------------------
# REDIRECT TO PAGES
# -------------------------------
elif page == "Baseline LSTM vs BiLSTM+Attention":
    st.switch_page("pages/1_Model_Experiments.py")

elif page == "VADER vs FinBERT":
    st.switch_page("pages/2_Sentiment_Comparison.py")

elif page == "Live Prediction":
    st.switch_page("pages/3_Live_Prediction.py")
