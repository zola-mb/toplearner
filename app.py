# app.py
import streamlit as st

st.set_page_config(page_title="Masi Dashboard", layout="wide")

p2024 = st.Page(
    "pages/2024/2024_top_learners.py",
    title="Top Learners (2024)",
    icon="📊",
    url_path="2024_top_learners",   # unique
)
p2025 = st.Page(
    "pages/2025/2025_top_learners.py",
    title="Top Learners (2025)",
    icon="📊",
    url_path="2025_top_learners",   # unique
)

nav = st.navigation({
    "2024": [p2024],
    "2025": [p2025],
})
nav.run()
