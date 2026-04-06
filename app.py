import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------
# 🎨 HIGH-CONTRAST HYBRID THEME
# ------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Force font on all elements */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', sans-serif !important;
}

/* 1. SEAMLESS TOP HEADER & PAGE CANVAS (Clean Light Grey) */
header[data-testid="stHeader"] {
    background-color: #f8fafc !important;
    border-bottom: 1px solid #e2e8f0;
}

.block-container {
    padding-top: 3rem !important;
    padding-bottom: 6rem !important;
    max-width: 1200px;
}

.stApp {
    background-color: #f8fafc !important;
}

/* 2. SIDEBAR: Ultra-Dark Command Center */
[data-testid="stSidebar"] {
    background-color: #05080f !important;
    border-right: 2px solid #1e293b !important;
}

[data-testid="stSidebar"] * {
    color: #94a3b8 !important;
}

/* Active navigation link in the sidebar */
[data-testid="stSidebarNav"] ul li div {
    background-color: #0f172a !important;
    border-radius: 8px !important;
}

/* High-contrast dark typography for the light page canvas */
h1 {
    font-weight: 800 !important;
    color: #0f172a !important;
    font-size: 2.8rem !important;
    margin-bottom: 0.5rem !important;
}

h2 {
    font-weight: 600 !important;
    color: #0284c7 !important;
    font-size: 1.5rem !important;
    margin-top: 1.5rem !important;
}

h3 {
    font-weight: 600 !important;
    color: #10b981 !important; /* Electric Emerald for a distinct module pop */
    font-size: 1.25rem !important;
    margin-bottom: 1rem !important;
}

/* 3. CARDS: Retained the dark, floating command blocks */
.cyber-card {
    background: #070a12 !important;
    padding: 1.8rem;
    border-radius: 16px;
    border: 1px solid #1e293b;
    box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3);
    margin-bottom: 1.5rem;
    height: 100%;
}

.cyber-card:hover {
    border: 1px solid #10b981;
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.15);
    transition: all 0.3s ease;
}

/* Text styling inside the dark cards */
.cyber-card p, .cyber-card span, .cyber-card li {
    color: #cbd5e1 !important;
    font-size: 14px;
    line-height: 1.6;
}

/* Custom Accents */
.subtitle {
    color: #64748b !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.metric-highlight {
    color: #10b981 !important;
    font-weight: 600 !important;
}

hr {
    border: 0;
    height: 1px;
    background: linear-gradient(to right, #e2e8f0, rgba(0,0,0,0));
    margin: 1.5rem 0;
}

/* 4. FOOTER: Deep pitch black to stand out at the bottom */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #05080f !important;
    color: #64748b !important;
    text-align: center;
    padding: 15px 0;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.2em;
    border-top: 1px solid #1e293b;
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 HOME PAGE
# -------------------------------

st.markdown('<p class="subtitle">FINANCIAL ANALYTICS DASHBOARD</p>', unsafe_allow_html=True)
st.title("🏠 About Capstone")
st.markdown("## 💡 AI-Driven Financial Sentiment Intelligence")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="cyber-card">
        <h3>📌 Overview</h3>
        <p>A system designed to extract <span class="metric-highlight">actionable insights from financial news</span> using advanced Natural Language Processing and deep learning models.</p>
    </div>
    """, unsafe_allow_html=True)

    # 🛠️ FIXED: Completely cleaned up to prevent ugly code blocks from rendering
    st.markdown("""
    <div class="cyber-card">
        <h3>⚙️ Core Modules</h3>
        <p style="font-weight:bold; color:#ffffff; margin-bottom:0.2rem;">Model Analysis</p>
        <ul style="padding-left: 1.2rem; margin-bottom:1rem;">
            <li>Baseline LSTM</li>
            <li>BiLSTM with Attention</li>
            <li>Captures contextual relationships in financial text</li>
        </ul>
        
        <p style="font-weight:bold; color:#ffffff; margin-bottom:0.2rem;">Sentiment Engine</p>
        <ul style="padding-left: 1.2rem; margin-bottom:1rem;">
            <li>VADER (rule-based)</li>
            <li>FinBERT (financial-domain model)</li>
            <li>Comparative performance evaluation</li>
        </ul>
        
        <p style="font-weight:bold; color:#ffffff; margin-bottom:0.2rem;">Prediction Interface</p>
        <ul style="padding-left: 1.2rem;">
            <li>Upload datasets</li>
            <li>Analyze sentiment</li>
            <li>Generate predictions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="cyber-card">
        <h3>📊 Capabilities</h3>
        <ul style="padding-left: 1.2rem;">
            <li>Sentiment classification (Positive / Neutral / Negative)</li>
            <li>Model comparison</li>
            <li>Interactive visualizations</li>
            <li>Dataset-driven insights</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cyber-card">
        <h3>🎯 Business Value</h3>
        <ul style="padding-left: 1.2rem;">
            <li>Faster interpretation of financial news</li>
            <li>Identification of sentiment-driven trends</li>
            <li>Better decision support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="cyber-card">
    <h3>🔁 Workflow</h3>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-top: 1rem;">
        <span style="background: #0f172a; color: #38bdf8; padding: 10px 20px; border-radius: 8px; font-size: 13px; font-weight: 600; border: 1px solid #1e293b;">1. Data Ingestion</span>
        <span style="color: #475569;">➔</span>
        <span style="background: #0f172a; color: #38bdf8; padding: 10px 20px; border-radius: 8px; font-size: 13px; font-weight: 600; border: 1px solid #1e293b;">2. Preprocessing</span>
        <span style="color: #475569;">➔</span>
        <span style="background: #0f172a; color: #38bdf8; padding: 10px 20px; border-radius: 8px; font-size: 13px; font-weight: 600; border: 1px solid #1e293b;">3. Model Analysis</span>
        <span style="color: #475569;">➔</span>
        <span style="background: #0f172a; color: #38bdf8; padding: 10px 20px; border-radius: 8px; font-size: 13px; font-weight: 600; border: 1px solid #1e293b;">4. Sentiment Eval</span>
        <span style="color: #475569;">➔</span>
        <span style="background: #10b981; color: #ffffff; padding: 10px 20px; border-radius: 8px; font-size: 13px; font-weight: 600;">5. Visualization</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# 📌 FOOTER
# -------------------------------
st.markdown(
    '<div class="footer">FINAL CAPSTONE PROJECT</div>',
    unsafe_allow_html=True
)
