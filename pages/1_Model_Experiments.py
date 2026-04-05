import streamlit as st
import nbformat
import base64

st.title("🤖 Model Experiments (v7.ipynb)")

def render_outputs_only(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            for output in cell.get("outputs", []):

                # 📊 SHOW PLOTS (matplotlib / seaborn)
                if "image/png" in output.get("data", {}):
                    img = output["data"]["image/png"]
                    st.image(base64.b64decode(img))

                # 📋 SHOW TABLES (pandas HTML)
                elif "text/html" in output.get("data", {}):
                    st.markdown(output["data"]["text/html"], unsafe_allow_html=True)

                # 🧾 OPTIONAL: show text results
                elif "text/plain" in output.get("data", {}):
                    st.text(output["data"]["text/plain"])

# Call function
render_outputs_only("v7.ipynb")
