import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide"
)

# -------------------------------
# 🎨 NEOBANK HIGH-CONTRAST LIGHT THEME
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

/* Apply font to the entire app */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #2D3748;
}

.stApp {
    background-color: #F7FAFC;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 5rem;
    max-width: 1200px;
}

/* Big gradient text for the main title */
h1 {
    font-weight: 800;
    font-size: 3rem !important;
    background: linear-gradient(to right, #4F46E5, #9333EA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem !important;
}

h2 {
    font-weight: 800;
    color: #1A202C;
    font-size: 1.6rem !important;
    margin-top: 1.5rem !important;
}

h3 {
    font-weight: 700;
    color: #4F46E5;
    font-size: 1.3rem !important;
    margin-top: 0.5rem !important;
    margin-bottom: 1rem !important;
}

/* Neobank Soft Shadow Cards */
.neo-card {
    background: #ffffff;
    padding: 2rem;
    border-radius: 20px;
    border: 1px solid #EDF2F7;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.03), 0 8px 10px -6px rgba(0, 0, 0, 0.03);
    margin-bottom: 1.5rem;
    height: 100%;
}

.neo-card:hover {
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
    transform: translateY(-2px);
    transition: all 0.3s ease;
}

.subtitle {
    color: #718096;
    font-weight: 600;
    font-size: 1rem;
    letter-spacing: 0.05em;
}

hr {
    border: 0;
    height: 1px;
    background: #E2E8F0;
    margin: 2rem 0;
}

.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #ffffff;
    color: #A0AEC0;
    text-align: center;
    padding: 15px 0;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.1em;
    border-top: 1px solid #EDF2F7;
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
    <div class="neo-card">
        <h3>📌 Overview</h3>
        <p style="color: #4A5568; line-height: 1.7;">A system designed to extract <b>actionable insights from financial news</b> using NLP and deep learning models.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neo-card">
        <h3>⚙️ Core Modules</h3>
        <p style="margin-bottom: 1.2rem;"><strong style="color: #2D3748;">Model Analysis</strong><br>
        <span style="color: #718096;">• Baseline LSTM<br>• BiLSTM with Attention<br>• Captures contextual relationships in financial text</span></p>
        
        <p style="margin-bottom: 1.2rem;"><strong style="color: #2D3748;">Sentiment Engine</strong><br>
        <span style="color: #718096;">• VADER (rule-based)<br>• FinBERT (financial-domain model)<br>• Comparative performance evaluation</span></p>
        
        <p><strong style="color: #2D3748;">Prediction Interface</strong><br>
        <span style="color: #718096;">• Upload datasets<br>• Analyze sentiment<br>• Generate predictions</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="neo-card">
        <h3>📊 Capabilities</h3>
        <ul style="color: #4A5568; line-height: 2;">
            <li>Sentiment classification (Positive / Neutral / Negative)</li>
            <li>Model comparison</li>
            <li>Interactive visualizations</li>
            <li>Dataset-driven insights</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neo-card">
        <h3>🎯 Business Value</h3>
        <ul style="color: #4A5568; line-height: 2;">
            <li>Faster interpretation of financial news</li>
            <li>Identification of sentiment-driven trends</li>
            <li>Better decision support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="neo-card">
    <h3>🔁 Workflow</h3>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-top: 1rem;">
        <span style="background: #EEF2F6; color: #4F46E5; padding: 12px 24px; border-radius: 12px; font-size: 14px; font-weight: 600;">1. Data ingestion</span>
        <span style="color: #CBD5E0; font-weight: bold;">➔</span>
        <span style="background: #EEF2F6; color: #4F46E5; padding: 12px 24px; border-radius: 12px; font-size: 14px; font-weight: 600;">2. Preprocessing</span>
        <span style="color: #CBD5E0; font-weight: bold;">➔</span>
        <span style="background: #EEF2F6; color: #4F46E5; padding: 12px 24px; border-radius: 12px; font-size: 14px; font-weight: 600;">3. Model analysis</span>
        <span style="color: #CBD5E0; font-weight: bold;">➔</span>
        <span style="background: #EEF2F6; color: #4F46E5; padding: 12px 24px; border-radius: 12px; font-size: 14px; font-weight: 600;">4. Sentiment evaluation</span>
        <span style="color: #CBD5E0; font-weight: bold;">➔</span>
        <span style="background: linear-gradient(to right, #4F46E5, #9333EA); color: #ffffff; padding: 12px 24px; border-radius: 12px; font-size: 14px; font-weight: 600;">5. Visualization</span>
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
