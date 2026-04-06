import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide"
)

# -------------------------------
# 🎨 CLASSY FINTECH UI STYLE
# -------------------------------
st.markdown("""
<style>
/* Import a clean, modern font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Apply font to the entire app */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
}

/* Background color for the whole app */
.stApp {
    background-color: #f8fafc;
}

/* Better spacing and max-width for readability */
.block-container {
    padding-top: 3rem;
    padding-bottom: 5rem;
    max-width: 1100px;
}

/* High-end Headings */
h1 {
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.025em;
    font-size: 2.5rem !important;
    margin-bottom: 0.5rem !important;
}

h2 {
    font-weight: 700;
    color: #1e293b;
    font-size: 1.75rem !important;
    margin-top: 2rem !important;
    margin-bottom: 1rem !important;
}

h3 {
    font-weight: 600;
    color: #334155;
    font-size: 1.25rem !important;
    margin-top: 1.5rem !important;
}

/* Custom Card Styling for Sections */
.fintech-card {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    margin-bottom: 1.5rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.fintech-card:hover {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

/* Styled Subtitles */
.subtitle {
    color: #0284c7;
    font-weight: 600;
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Subtle divider */
hr {
    border: 0;
    height: 1px;
    background-color: #e2e8f0;
    margin: 2rem 0;
}

/* Footer with a more modern, minimal look */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #ffffff;
    color: #94a3b8;
    text-align: center;
    padding: 12px 0;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    border-top: 1px solid #e2e8f0;
    z-index: 999;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 HOME PAGE
# -------------------------------

# Top Accent & Title
st.markdown('<p class="subtitle">Financial Analytics Dashboard</p>', unsafe_allow_html=True)
st.title("🏠 About Capstone")

st.markdown("## 💡 AI-Driven Financial Sentiment Intelligence")
st.markdown("---")

# Using Streamlit columns combined with our custom CSS classes for a grid layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="fintech-card">
        <h3>📌 Overview</h3>
        <p style="color: #64748b;">A system designed to extract <strong>actionable insights from financial news</strong> using NLP and deep learning models.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fintech-card">
        <h3>⚙️ Core Modules</h3>
        <p><strong>Model Analysis</strong><br>
        • Baseline LSTM<br>
        • BiLSTM with Attention<br>
        • Captures contextual relationships in financial text</p>
        
        <p><strong>Sentiment Engine</strong><br>
        • VADER (rule-based)<br>
        • FinBERT (financial-domain model)<br>
        • Comparative performance evaluation</p>
        
        <p><strong>Prediction Interface</strong><br>
        • Upload datasets<br>
        • Analyze sentiment<br>
        • Generate predictions</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="fintech-card">
        <h3>📊 Capabilities</h3>
        <p style="margin-bottom: 0.5rem;">• Sentiment classification (Positive / Neutral / Negative)</p>
        <p style="margin-bottom: 0.5rem;">• Model comparison</p>
        <p style="margin-bottom: 0.5rem;">• Interactive visualizations</p>
        <p style="margin-bottom: 0.5rem;">• Dataset-driven insights</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fintech-card">
        <h3>🎯 Business Value</h3>
        <p style="margin-bottom: 0.5rem;">• Faster interpretation of financial news</p>
        <p style="margin-bottom: 0.5rem;">• Identification of sentiment-driven trends</p>
        <p style="margin-bottom: 0.5rem;">• Better decision support</p>
    </div>
    """, unsafe_allow_html=True)

# Full width workflow card at the bottom
st.markdown("""
<div class="fintech-card">
    <h3>🔁 Workflow</h3>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-top: 1rem;">
        <span style="background: #f1f5f9; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: 500;">1. Data ingestion</span>
        <span style="color: #cbd5e1;">➔</span>
        <span style="background: #f1f5f9; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: 500;">2. Preprocessing</span>
        <span style="color: #cbd5e1;">➔</span>
        <span style="background: #f1f5f9; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: 500;">3. Model analysis</span>
        <span style="color: #cbd5e1;">➔</span>
        <span style="background: #f1f5f9; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: 500;">4. Sentiment evaluation</span>
        <span style="color: #cbd5e1;">➔</span>
        <span style="background: #f1f5f9; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: 500;">5. Visualization</span>
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
