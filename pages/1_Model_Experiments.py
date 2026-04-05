import streamlit as st
import nbformat
from nbconvert import HTMLExporter

st.title("🤖 Model Experiments (v7.ipynb)")

def render_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    html_exporter.template_name = "classic"

    (body, resources) = html_exporter.from_notebook_node(notebook)

    st.components.v1.html(body, height=800, scrolling=True)

# Load your notebook
render_notebook("v7.ipynb")
