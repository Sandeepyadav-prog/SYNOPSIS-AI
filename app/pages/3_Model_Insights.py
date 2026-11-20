
import streamlit as st
import pandas as pd
from pathlib import Path

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
.insight-header {
    background: linear-gradient(115deg, #102A43, #176B78);
    padding: 27px 30px;
    border-radius: 15px;
    margin-bottom: 24px;
}
.insight-header h1 {
    color: white;
    font-size: 29px;
}
.insight-header p {
    color: #DCEAF0;
    font-size: 14px;
}
.info-card {
    background: white;
    border: 1px solid #E5EBF1;
    border-radius: 13px;
    padding: 19px;
    min-height: 120px;
}
.card-label {
    color: #718096;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}
.card-value {
    color: #102A43;
    font-size: 21px;
    font-weight: 750;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="insight-header">
    <h1>📊 Model Insights</h1>
    <p>Explore the architecture, technology and evaluation
    methodology behind SYNOPSIS AI.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Model Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <div class="card-label">MODEL</div>
        <div class="card-value">DistilBART</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <div class="card-label">MODEL TYPE</div>
        <div class="card-value">Transformer</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <div class="card-label">TASK</div>
        <div class="card-value">Summarization</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.subheader("About BART")

st.write("""
BART (Bidirectional and Auto-Regressive Transformers) is a
sequence-to-sequence Transformer architecture.

It combines a bidirectional encoder with an autoregressive
decoder. This allows the model to understand the input text
and generate a new summary in natural language.

Our project uses the pretrained distilled BART model:
`sshleifer/distilbart-cnn-12-6`.
""")

st.subheader("Model Configuration")

config = pd.DataFrame({
    "Parameter": [
        "Model",
        "Architecture",
        "Maximum Input Tokens",
        "Beam Search",
        "Inference Framework",
        "Pretraining / Fine-tuning"
    ],
    "Configuration": [
        "DistilBART CNN 12-6",
        "Encoder-Decoder Transformer",
        "1024",
        "4 beams",
        "PyTorch",
        "CNN/DailyMail summarization"
    ]
})

st.dataframe(config, use_container_width=True, hide_index=True)

st.write("")
st.subheader("How the Model Works")

steps = [
    ("01", "Input Text", "The user provides an article or document."),
    ("02", "Tokenization", "Text is converted into numerical tokens."),
    ("03", "Transformer Encoder", "The encoder understands context and relationships."),
    ("04", "Transformer Decoder", "The decoder generates a concise summary."),
    ("05", "Final Summary", "The generated summary is displayed to the user.")
]

for number, title, description in steps:
    with st.container(border=True):
        col1, col2 = st.columns([1, 8])
        with col1:
            st.markdown(f"### {number}")
        with col2:
            st.markdown(f"**{title}**")
            st.caption(description)

st.write("")
st.subheader("ROUGE Evaluation")

st.write("""
ROUGE is used to compare generated summaries with reference
summaries written by humans.
""")

project_root = Path(__file__).resolve().parents[2]
results_file = project_root / "dataset" / "rouge_evaluation_results.csv"

if results_file.exists():
    results = pd.read_csv(results_file)

    metric_columns = ["rouge1", "rouge2", "rougeL"]
    available = [col for col in metric_columns if col in results.columns]

    if available:
        averages = results[available].mean()

        a, b, c = st.columns(3)

        for column, label in zip(
            [a, b, c],
            ["ROUGE-1", "ROUGE-2", "ROUGE-L"]
        ):
            with column:
                if label.lower().replace("-", "") in [
                    x.lower().replace("-", "") for x in available
                ]:
                    matching = next(
                        x for x in available
                        if x.lower().replace("-", "") ==
                        label.lower().replace("-", "")
                    )
                    st.metric(label, f"{averages[matching]:.4f}")

        st.bar_chart(averages)

        st.caption(
            f"Evaluation records available: {len(results)}"
        )
    else:
        st.warning("ROUGE columns were not found in the results file.")
else:
    st.info(
        "ROUGE evaluation results will appear here after the "
        "model evaluation script has generated the results CSV."
    )

st.markdown("---")
st.caption("SYNOPSIS AI | Model Insights")
