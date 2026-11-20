
import streamlit as st

st.set_page_config(
    page_title="SYNOPSIS AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

home = st.Page(
    "pages/1_Home_Dashboard.py",
    title="Home Dashboard",
    icon="🏠",
    default=True
)

summarizer = st.Page(
    "pages/2_AI_Summarizer.py",
    title="AI Summarizer",
    icon="✦"
)
insights = st.Page(
    "pages/3_Model_Insights.py",
    title="Model Insights",
    icon="📊"
)
workflow = st.Page(
    "pages/4_How_It_Works.py",
    title="How It Works",
    icon="⚙️"
)
about = st.Page(
    "pages/5_About_Project.py",
    title="About Project",
    icon="🎓"
)
history = st.Page(
    "pages/6_Summary_History.py",
    title="Summary History",
    icon="📚"
)

pg = st.navigation({
    "MAIN MENU": [home, summarizer],
    "ANALYTICS": [insights, workflow],
    "INFORMATION": [about, history]
})

pg.run()

pg.run()
