import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# 🎨 CUSTOM DUO-TONE CYBER THEME
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Apply font to the entire app */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', sans-serif;
    color: #e2e8f0;
}

/* 1. Main background (Lighter, but still dark/vibrant) */
.stApp {
    background-color: #111625;
    background-image: radial-gradient(circle at top right, #1a233a, #111625);
}

/* 2. Sidebar background (Deepest Navy) */
[data-testid="stSidebar"] {
    background-color: #090d16 !important;
    border-right: 1px solid rgba(56, 189, 248, 0.1);
}

/* Fix sidebar text color so it's readable against the dark background */
[data-testid="stSidebar"] * {
    color: #94a3b8 !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #e2e8f0 !important;
}

/* Fix for the cut-off title (gives enough space at the top) */
.block-container {
    padding-top: 5rem !important;
    padding-bottom: 5rem;
    max-width: 1200px;
}

/* Typography */
h1 {
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.03em;
    font-size: 2.8rem !important;
    margin-bottom: 0.5rem !important;
    line-height: 1.2 !important; /* Prevents text clipping */
}

h2 {
    font-weight: 600;
    color: #38bdf8;
    font-size: 1.5rem !important;
    margin-top: 1.5rem !important;
    letter-spacing: -0.01em;
}

h3 {
    font-weight: 600;
    color: #06b6d4;
    font-size: 1.2rem !important;
    margin-top: 0.5rem !important;
    margin-bottom: 1rem !important;
}

/* Glowing Cards (Slightly darker than main page to create depth) */
.cyber-card {
    background: rgba(9, 13, 22, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 1.8rem;
    border-radius: 16px;
    border: 1px solid rgba(56, 189, 248, 0.15);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-bottom: 1.5rem;
    height: 100%;
}

.cyber-card:hover {
    border: 1px solid rgba(56, 189, 248, 0.3);
    box-shadow: 0 8px 32px 0 rgba(56, 189, 248, 0.08);
    transform: translateY(-2px);
    transition: all 0.3s ease;
}

/* Accent texts */
.subtitle {
    color: #a5b4fc;
    font-weight: 600;
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.metric-highlight {
    color: #34d399;
    font-weight: 600;
}

/* Custom horizontal rule */
hr {
    border: 0;
    height: 1px;
    background: linear-gradient(to right, rgba(56, 189, 248, 0.5), rgba(0,0,0,0));
    margin: 1.5rem 0;
}

/* Footer (Blending with main content background) */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgba(17, 22, 37, 0.95);
    backdrop-filter: blur(5px);
    color: #64748b;
    text-align: center;
    padding: 12px 0;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    border-top: 1px solid rgba(56, 189, 248, 0.1);
    z-index: 999;
}

.stMarkdown em {
    color: #fbbf24;
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
        <p style="color: #94a3b8; line-height: 1.6;">A system designed to extract <span class="metric-highlight">actionable insights from financial news</span> using advanced Natural Language Processing and deep learning models.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cyber-card">
        <h3>⚙️ Core Modules</h3>
        <p style="margin-bottom: 1rem;"><strong style="color:#f8fafc;">Model Analysis</strong><br>
        <span style="color:#94a3b8;">• Baseline LSTM<br>• BiLSTM with Attention<br>• Captures contextual relationships in financial text</span></p>
        
        <p style="margin-bottom: 1rem;"><strong style="color:#f8fafc;">Sentiment Engine</strong><br>
        <span style="color:#94a3b8;">• VADER (rule-based)<br>• FinBERT (financial-domain model)<br>• Comparative performance evaluation</span></p>
        
        <p><strong style="color:#f8fafc;">Prediction Interface</strong><br>
        <span style="color:#94a3b8;">• Upload datasets<br>• Analyze sentiment<br>• Generate predictions</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="cyber-card">
        <h3>📊 Capabilities</h3>
        <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 8px; margin-bottom: 10px; border-left: 3px solid #06b6d4;">
            <p style="margin-bottom: 0; color: #f8fafc; font-size: 14px;">⚡ Sentiment classification (Positive / Neutral / Negative)</p>
        </div>
        <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 8px; margin-bottom: 10px; border-left: 3px solid #06b6d4;">
            <p style="margin-bottom: 0; color: #f8fafc; font-size: 14px;">📈 Model comparison</p>
        </div>
        <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 8px; margin-bottom: 10px; border-left: 3px solid #06b6d4;">
            <p style="margin-bottom: 0; color: #f8fafc; font-size: 14px;">🎯 Interactive visualizations</p>
        </div>
        <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 8px; border-left: 3px solid #06b6d4;">
            <p style="margin-bottom: 0; color: #f8fafc; font-size: 14px;">🗂️ Dataset-driven insights</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cyber-card">
        <h3>🎯 Business Value</h3>
        <p style="color: #94a3b8; line-height: 1.6;">• Faster interpretation of financial news<br>
        • Identification of sentiment-driven trends<br>
        • Better decision support</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="cyber-card">
    <h3>🔁 Workflow</h3>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-top: 1rem;">
        <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; border: 1px solid rgba(56, 189, 248, 0.2);">1. Data Ingestion</span>
        <span style="color: #64748b;">➔</span>
        <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; border: 1px solid rgba(56, 189, 248, 0.2);">2. Preprocessing</span>
        <span style="color: #64748b;">➔</span>
        <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; border: 1px solid rgba(56, 189, 248, 0.2);">3. Model Analysis</span>
        <span style="color: #64748b;">➔</span>
        <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; border: 1px solid rgba(56, 189, 248, 0.2);">4. Sentiment Eval</span>
        <span style="color: #64748b;">➔</span>
        <span style="background: #059669; color: #ffffff; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600;">5. Visualization</span>
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
