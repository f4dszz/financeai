"""
FinanceAI Platform - Streamlit Frontend
Last Updated: 2024-12-14 21:00
"""

import os

import streamlit as st

# === Page Configuration ===
st.set_page_config(
    page_title="FinanceAI Platform",
    page_icon="F",
    layout="wide",
    initial_sidebar_state="expanded",
)

# === Constants ===
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# === Main Page ===
st.title("FinanceAI Platform")
st.markdown("### Compliance/Risk AI Copilot")

st.markdown("---")

# === Status Cards ===
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="RAG Q&A", value="Week 2", delta="Planned")

with col2:
    st.metric(label="Chart OCR", value="Week 3", delta="Planned")

with col3:
    st.metric(label="Anomaly Detection", value="Week 4", delta="Planned")

st.markdown("---")

# === Navigation ===
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- **Home**: This page
- **Q&A**: Regulatory document Q&A (Week 2)
- **Chart**: Financial chart extraction (Week 3)
- **Anomaly**: Trading anomaly detection (Week 4)
""")

# === Disclaimer ===
st.markdown("---")
st.warning("""
**Disclaimer / 免责声明**

This content is AI-generated for reference only and does not constitute investment advice.
Please consult licensed professionals for financial decisions.

本内容由AI生成，仅供参考，不构成任何投资建议。金融决策请咨询持牌专业人士。
""")

# === Footer ===
st.markdown("---")
st.markdown(
    f"Backend: `{BACKEND_URL}` | "
    "[API Docs](http://localhost:8000/docs) | "
    "Built with Streamlit"
)
