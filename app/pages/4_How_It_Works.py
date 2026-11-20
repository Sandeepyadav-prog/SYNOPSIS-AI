
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
.workflow-header {
    background: linear-gradient(115deg, #102A43, #176B78);
    padding: 27px 30px;
    border-radius: 15px;
    margin-bottom: 24px;
}
.workflow-header h1 {
    color: white;
    font-size: 29px;
}
.workflow-header p {
    color: #DCEAF0;
    font-size: 14px;
}
.step-card {
    background: white;
    border: 1px solid #E5EBF1;
    border-radius: 13px;
    padding: 19px;
    margin-bottom: 12px;
}
.step-number {
    color: #159A91;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1px;
}
.step-title {
    color: #102A43;
    font-size: 18px;
    font-weight: 750;
    margin: 6px 0;
}
.step-description {
    color: #718096;
    font-size: 13px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="workflow-header">
    <h1>⚙️ How SYNOPSIS AI Works</h1>
    <p>Explore the complete pipeline behind AI-powered
    abstractive text summarization.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("System Workflow")
st.caption("From raw news articles to meaningful AI-generated summaries.")

steps = [
    (
        "01",
        "Dataset Collection",
        "The CNN/DailyMail dataset provides news articles and their "
        "human-written reference summaries."
    ),
    (
        "02",
        "Exploratory Data Analysis",
        "The dataset is examined to understand article lengths, "
        "summary lengths and missing values."
    ),
    (
        "03",
        "Text Preprocessing",
        "Missing records are removed and unnecessary whitespace "
        "is normalized while preserving natural language."
    ),
    (
        "04",
        "Tokenization",
        "The tokenizer converts the input text into numerical tokens "
        "that the Transformer model can process."
    ),
    (
        "05",
        "Transformer Processing",
        "The DistilBART encoder processes the input context and "
        "the decoder generates a concise summary."
    ),
    (
        "06",
        "Summary Generation",
        "Beam search helps the model generate a coherent summary "
        "according to the selected length."
    ),
    (
        "07",
        "Model Evaluation",
        "Generated summaries are compared with reference summaries "
        "using ROUGE-1, ROUGE-2 and ROUGE-L."
    ),
    (
        "08",
        "Final Output",
        "The website displays the generated summary, word counts "
        "and text reduction, with an option to download the result."
    )
]

for number, title, description in steps:
    st.markdown(f"""
    <div class="step-card">
        <div class="step-number">WORKFLOW STEP {number}</div>
        <div class="step-title">{title}</div>
        <div class="step-description">{description}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.subheader("Technology Stack")

tech1, tech2 = st.columns(2)

with tech1:
    st.container(border=True).markdown("""
    **Machine Learning & NLP**

    - Python
    - Hugging Face Transformers
    - DistilBART
    - PyTorch
    - ROUGE Evaluation
    """)

with tech2:
    st.container(border=True).markdown("""
    **Data & Application**

    - CNN/DailyMail Dataset
    - Pandas
    - Matplotlib
    - Seaborn
    - Streamlit
    """)

st.write("")
st.info(
    "The project uses a pretrained DistilBART model fine-tuned "
    "for CNN/DailyMail summarization. It does not train BART "
    "from scratch."
)

st.markdown("---")
st.caption("SYNOPSIS AI | Understanding the AI Workflow")
