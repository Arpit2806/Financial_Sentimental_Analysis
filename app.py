import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------
# 🎨 UNIFIED SEAMLESS CYBER THEME
# ------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Force font on all elements */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', sans-serif !important;
}

/* 1. SEAMLESS BACKGROUND (No more blocky sidebar!) */
.stApp, [data-testid="stSidebar"] {
    background-color: #0b0f19 !important;
    background-image: radial-gradient(circle at top right, #1a233a, #0b0f19) !important;
}

/* Make the line dividing sidebar and page invisible for a true borderless look */
[data-testid="stSidebar"] {
    border-right: none !important;
}

/* 2. BRIGHTER SIDEBAR TEXT */
[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* Active navigation item styling */
[data-testid="stSidebarNav"] ul li div {
    border-radius: 8px !important;
}

/* 3. FIX TITLE CLIPPING & PADDING */
.block-container {
    padding-top: 6rem !important;
    padding-bottom: 5rem !important;
    max-width: 1200px;
}

/* High-contrast typography */
h1 {
    font-weight: 800 !important;
    color: #ffffff !important;
    letter-spacing: -0.03em !important;
    font-size: 2.8rem !important;
    margin-bottom: 0.5rem !important;
    line-height: 1.4 !important;
}

h2 {
    font-weight: 600 !important;
    color: #38bdf8 !important;
    font-size: 1.5rem !important;
    margin-top: 1.5rem !important;
}

h3 {
    font-weight: 600 !important;
    color: #06b6d4 !important;
    font-size: 1.25rem !important;
    margin-bottom: 1rem !important;
}

/* Glowing Cards */
.cyber-card {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 1.8rem;
    border-radius: 16px;
    border: 1px solid rgba(56, 189, 248, 0.15);
    box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.4);
    margin-bottom: 1.5rem;
    height: 100%;
}

.cyber-card:hover {
    border: 1px solid rgba(56, 189, 248, 0.3);
    box-shadow: 0 4px 20px 0 rgba(56, 189, 248, 0.05);
    transform: translateY(-2px);
    transition: all 0.3s ease;
}

/* Accents */
.subtitle {
    color: #a5b4fc !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.metric-highlight {
    color: #34d399 !important;
    font-weight: 600 !important;
}

/* Custom horizontal rule */
hr {
    border: 0;
    height: 1px;
    background: linear-gradient(to right, rgba(56, 189, 248, 0.5), rgba(0,0,0,0));
    margin: 1.5rem 0;
}

/* Footer */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgba(11, 15, 25, 0.95);
    backdrop-filter: blur(5px);
    color: #64748b;
    text-align: center;
    padding: 12px 0;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    border-top: 1px solid rgba(255,255,255,0.05);
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)

# Fake sidebar content just so the active page marker has a reference
with st.sidebar:
    st.markdown(" ") # Spacer to respect top layout

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

st.markdown(
    '<div class="footer">FINAL CAPSTONE PROJECT</div>',
    unsafe_allow_html=True
)
