
import streamlit as st

st.markdown("""
<style>
.stApp {
    background: #F5F7FA;
    color: #172B4D;
}
.block-container {
    max-width: 1350px;
    padding: 1.5rem 2.5rem 2rem 2.5rem;
}
section[data-testid="stSidebar"] {
    background: #102A43;
}
section[data-testid="stSidebar"] * {
    color: white;
}
.about-header {
    background: linear-gradient(115deg, #102A43, #176B78);
    padding: 28px 30px;
    border-radius: 15px;
    margin-bottom: 24px;
}
.about-header h1 {
    color: white;
    font-size: 29px;
}
.about-header p {
    color: #DCEAF0;
    font-size: 14px;
}
.about-card {
    background: white;
    border: 1px solid #E5EBF1;
    border-radius: 13px;
    padding: 20px;
    margin-bottom: 12px;
}
.card-title {
    color: #176B78;
    font-size: 16px;
    font-weight: 750;
    margin-bottom: 9px;
}
.card-description {
    color: #627789;
    font-size: 13px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-header">
    <h1>🎓 About SYNOPSIS AI</h1>
    <p>Learn about the vision, objectives and technology
    behind our AI-powered summarization platform.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Project Introduction")

st.write("""
**AI-Powered Abstractive Text Summarization** is a Natural
Language Processing project that converts lengthy articles
and documents into shorter, meaningful summaries.

The application uses a pretrained DistilBART Transformer
model fine-tuned for news summarization to understand
context and generate natural-language summaries.
""")

st.write("")
st.subheader("Problem Statement")

with st.container(border=True):
    st.write("""
    In the digital world, people encounter large amounts of
    textual information every day. Reading lengthy articles,
    reports and documents requires considerable time.

    Traditional keyword-based methods may miss important
    contextual information. Therefore, an intelligent system
    is needed to generate concise summaries while preserving
    the main meaning of the original content.
    """)

st.write("")
st.subheader("Project Objectives")

objectives = [
    "Develop an AI-powered abstractive text summarization application.",
    "Use Transformer-based deep learning for natural-language generation.",
    "Process and analyze the CNN/DailyMail dataset.",
    "Generate summaries with adjustable output lengths.",
    "Evaluate summarization quality using ROUGE metrics.",
    "Provide a simple and interactive web interface."
]

for item in objectives:
    st.markdown(f"- {item}")

st.write("")
st.subheader("Key Features")

features = [
    ("AI-Based Summarization",
     "Generate concise summaries from lengthy text."),
    ("Adjustable Summary Length",
     "Choose Short, Medium or Long summaries."),
    ("Document Input",
     "Paste text or upload a TXT document."),
    ("Summary Statistics",
     "View original words, summary words and text reduction."),
    ("Download Results",
     "Download the generated summary as a text file."),
    ("Model Evaluation",
     "Explore ROUGE-based evaluation results.")
]

for i in range(0, len(features), 2):
    left, right = st.columns(2)

    with left:
        title, description = features[i]
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.caption(description)

    if i + 1 < len(features):
        with right:
            title, description = features[i + 1]
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(description)

st.write("")
st.subheader("Technology Stack")

technologies = {
    "Programming Language": "Python",
    "Deep Learning": "PyTorch",
    "Transformer Library": "Hugging Face Transformers",
    "AI Model": "DistilBART CNN 12-6",
    "Dataset": "CNN/DailyMail",
    "Data Processing": "Pandas, NumPy",
    "Data Visualization": "Matplotlib, Seaborn",
    "Web Framework": "Streamlit",
    "Evaluation": "ROUGE-1, ROUGE-2, ROUGE-L"
}

st.table(technologies)

st.write("")
st.subheader("Real-World Applications")

applications = [
    "News article summarization",
    "Research paper summarization",
    "Business report summarization",
    "Educational content summarization",
    "Information management"
]

for app in applications:
    st.markdown(f"- {app}")

st.write("")
st.success(
    "Our goal is to make information easier to understand "
    "by reducing lengthy content into meaningful insights."
)

st.markdown("---")
st.caption("SYNOPSIS AI | AI-Powered Abstractive Text Summarization")
