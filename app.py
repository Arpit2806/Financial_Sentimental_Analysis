import streamlit as st

st.set_page_config(
    page_title="Financial Sentiment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------
# 🎨 LAYOUT ONLY THEME (Matches your screenshot)
# ------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Force clean font on the whole app */
html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', sans-serif !important;
}

/* 1. FORCE HEADER TO BLEND WITH WHITE CANVAS */
header[data-testid="stHeader"] {
    background-color: #ffffff !important;
    border-bottom: none !important;
}

/* 2. MAIN PAGE CANVAS: Pure Clean White */
.stApp {
    background-color: #ffffff !important;
}

/* Perfect alignment for content on the white canvas */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 5rem !important;
    max-width: 1200px;
}

/* 3. SIDEBAR: Solid Dark Navy/Black */
[data-testid="stSidebar"] {
    background-color: #0d1527 !important;
    border-right: none !important;
}

/* Navigation text in sidebar */
[data-testid="stSidebarNav"] ul li div a span {
    color: #94a3b8 !important;
    font-size: 14px !important;
}

/* Active navigation item background highlight */
[data-testid="stSidebarNav"] ul li div {
    background-color: #1a2438 !important;
    border-radius: 4px !important;
}

/* Top "app" indicator box in your sidebar */
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #94a3b8 !important;
    font-size: 14px;
}

/* 4. FOOTER: Pitch black pinned bar */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #0a0f1d !important;
    color: #475569 !important;
    text-align: center;
    padding: 10px 0;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    border-top: 1px solid #1e293b;
    z-index: 999;
}

/* High contrast typography for the white canvas */
h1 {
    color: #1e293b !important;
    font-weight: 800 !important;
    font-size: 2.6rem !important;
    margin-bottom: 0.5rem !important;
}

h2 {
    color: #334155 !important;
    font-weight: 700 !important;
    font-size: 1.6rem !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🏠 CONTENT (Simplified to test layout)
# -------------------------------

st.title("🏠 About Capstone")
st.markdown("## 💡 AI-Driven Financial Sentiment Intelligence")
st.markdown("---")

st.markdown("### 📌 Overview")
st.markdown("""
This project builds a **financial sentiment intelligence system** that transforms unstructured news data into meaningful market insights.

It leverages:
* Deep Learning (LSTM, BiLSTM + Attention)
* NLP techniques for text understanding
* Financial-domain sentiment analysis
""")

# -------------------------------
# 📌 FOOTER
# -------------------------------
st.markdown(
    '<div class="footer">FINAL CAPSTONE PROJECT</div>',
    unsafe_allow_html=True
)
