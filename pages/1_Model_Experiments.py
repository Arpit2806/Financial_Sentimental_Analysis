import streamlit as st
import nbformat
import base64

st.title("🤖 Model Experiments (LSTM + Attention)")

def render_clean_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    current_section = "📊 Analysis"

    for cell in nb.cells:

        # 🧠 Use markdown as section titles
        if cell.cell_type == "markdown":
            text = "".join(cell.source)

            # pick only headings
            if text.strip().startswith("#"):
                current_section = text.replace("#", "").strip()
                st.subheader(current_section)

        # 📊 Show only outputs from code cells
        elif cell.cell_type == "code":
            for output in cell.get("outputs", []):

                data = output.get("data", {})

                # Show plots
                if "image/png" in data:
                    img = base64.b64decode(data["image/png"])
                    st.image(img, use_container_width=True)

                # Show tables
                elif "text/html" in data:
                    st.markdown(data["text/html"], unsafe_allow_html=True)

                # Skip raw text to keep UI clean

# 🔥 Call function
render_clean_notebook("v7.ipynb")
