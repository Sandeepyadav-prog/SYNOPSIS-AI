
import sys
import json
import html
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from xml.sax.saxutils import escape
from io import BytesIO
from pathlib import Path
from datetime import datetime
from io import BytesIO

def create_summary_pdf(summary, original_words, summary_words, reduction):
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        textColor=HexColor("#102A43"),
        fontSize=22,
        spaceAfter=15
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontSize=11,
        leading=17,
        textColor=HexColor("#12344A"),
        spaceAfter=10
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        textColor=HexColor("#176B78"),
        spaceBefore=12,
        spaceAfter=8
    )

    story = [
        Paragraph("SYNOPSIS AI", title_style),
        Paragraph("AI-Generated Text Summary", heading_style),
        Spacer(1, 10),
        Paragraph("Generated Summary", heading_style)
    ]

    safe_summary = escape(summary).replace("\n", "<br/>")

    story.append(Paragraph(safe_summary, body_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Summary Statistics", heading_style))

    story.append(
        Paragraph(
            f"Original Words: {original_words}<br/>"
            f"Summary Words: {summary_words}<br/>"
            f"Text Reduction: {reduction:.1f}%",
            body_style
        )
    )

    story.append(Spacer(1, 25))
    story.append(
        Paragraph(
            "Generated using DistilBART Transformer Model | SYNOPSIS AI",
            styles["Italic"]
        )
    )

    document.build(story)

    buffer.seek(0)
    return buffer.getvalue()


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import streamlit as st
from utils.summarizer import summarize_text
from pypdf import PdfReader
from docx import Document

HISTORY_FILE = ROOT / "dataset" / "summary_history.json"


# ---------------------------------------
# DOCUMENT TEXT EXTRACTION
# ---------------------------------------

def extract_pdf_text(file):
    reader = PdfReader(BytesIO(file.getvalue()))
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return "\n".join(pages)


def extract_docx_text(file):
    document = Document(BytesIO(file.getvalue()))

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs)


# ---------------------------------------
# HISTORY STORAGE
# ---------------------------------------

def save_to_history(original, summary, length):
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    history = []

    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)

            if not isinstance(history, list):
                history = []

        except (json.JSONDecodeError, OSError):
            history = []

    history.append({
        "original": original,
        "summary": summary,
        "length": length,
        "date": datetime.now().strftime("%d %b %Y, %I:%M %p")
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


# ---------------------------------------
# PAGE STYLING
# ---------------------------------------

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

.page-header {
    background: linear-gradient(115deg, #102A43, #176B78);
    padding: 25px 30px;
    border-radius: 15px;
    margin-bottom: 23px;
}

.page-header h1 {
    color: white;
    font-size: 29px;
    margin-bottom: 8px;
}

.page-header p {
    color: #DCEAF0;
    font-size: 14px;
}

.section-card {
    background: white;
    border: 1px solid #E5EBF1;
    padding: 20px;
    border-radius: 13px;
    box-shadow: 0 3px 12px rgba(16,42,67,0.035);
}

.result-card {
    background: #E8F5F4;
    border: 1px solid #C7E8E4;
    padding: 22px;
    border-radius: 13px;
}

.result-title {
    color: #176B78;
    font-weight: 700;
    font-size: 15px;
    margin-bottom: 12px;
}

.result-text {
    color: #12344A;
    font-size: 15px;
    line-height: 1.8;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
}

.small-label {
    color: #718096;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

.metric-number {
    color: #102A43;
    font-size: 22px;
    font-weight: 750;
}

.stButton > button {
    background: #147D79;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    min-height: 42px;
}

.stButton > button:hover {
    background: #10645F;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------
# HEADER
# ---------------------------------------

st.markdown("""
<div class="page-header">
    <h1>✦ AI Text Summarizer</h1>
    <p>Convert lengthy text into clear and meaningful summaries
    using our Transformer-powered BART model.</p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------
# MODEL INFORMATION
# ---------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="section-card">
        <div class="small-label">MODEL</div>
        <div class="metric-number">DistilBART</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="section-card">
        <div class="small-label">METHOD</div>
        <div class="metric-number">Abstractive</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="section-card">
        <div class="small-label">FRAMEWORK</div>
        <div class="metric-number">PyTorch</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------
# INPUT WORKSPACE
# ---------------------------------------

st.write("")
st.subheader("Create Your Summary")
st.caption("Paste your content or upload a TXT, PDF, or Word document.")

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["txt", "pdf", "docx"],
    help="Supported formats: TXT, PDF and DOCX."
)

uploaded_text = ""

if uploaded_file is not None:
    try:
        file_extension = Path(uploaded_file.name).suffix.lower()

        if file_extension == ".txt":
            uploaded_text = uploaded_file.getvalue().decode(
                "utf-8", errors="replace"
            )

        elif file_extension == ".pdf":
            uploaded_text = extract_pdf_text(uploaded_file)

        elif file_extension == ".docx":
            uploaded_text = extract_docx_text(uploaded_file)

        if not uploaded_text.strip():
            st.warning(
                "No readable text was found. "
                "The PDF may be scanned or the document may be empty."
            )
        else:
            st.success(
                f"Successfully extracted text from {uploaded_file.name}"
            )

    except Exception as e:
        st.error(f"Unable to read the uploaded document: {e}")


if "article_input" not in st.session_state:
    st.session_state.article_input = ""

if "last_uploaded_file" not in st.session_state:
    st.session_state.last_uploaded_file = None

if uploaded_file is not None:
    if st.session_state.last_uploaded_file != uploaded_file.name:
        st.session_state.article_input = uploaded_text
        st.session_state.last_uploaded_file = uploaded_file.name

# ---------------------------------------
# SAMPLE ARTICLES LIBRARY
# ---------------------------------------

sample_articles = {
    "Artificial Intelligence": """Artificial Intelligence is transforming modern industries by enabling machines to perform tasks that traditionally require human intelligence. AI systems can analyze large amounts of data, recognize patterns, automate repetitive work, and support decision-making. Industries such as healthcare, education, banking, and transportation are using AI to improve efficiency and services. However, AI also creates challenges related to privacy, security, employment, and ethical responsibility. Responsible development and human supervision are essential to ensure that AI benefits society.""",

    "Climate Change": """Climate change is one of the major environmental challenges facing the world. Rising temperatures, melting glaciers, changing rainfall patterns, and extreme weather events are affecting ecosystems and human communities. Human activities such as burning fossil fuels, deforestation, and industrial pollution contribute significantly to greenhouse gas emissions. Governments and organizations are promoting renewable energy, sustainable transportation, and forest conservation to reduce environmental damage. Individual actions, combined with international cooperation, can help build a more sustainable future.""",

    "Digital Education": """Digital education has changed how students access knowledge and develop skills. Online learning platforms, virtual classrooms, recorded lectures, and educational applications allow students to learn from different locations. Technology also provides interactive exercises and personalized learning opportunities. However, unequal internet access, digital distractions, and limited face-to-face interaction remain important challenges. Schools and universities should combine digital tools with effective teaching practices to create inclusive and engaging learning environments."""
}

st.markdown("### 📚 Try a Sample Article")
st.caption("Choose a sample topic and load its content into the text editor.")

selected_sample = st.selectbox(
    "Select a sample topic",
    list(sample_articles.keys())
)

if st.button("Load Sample Article"):
    st.session_state.article_input = sample_articles[selected_sample]
    st.session_state.last_uploaded_file = None
    st.success(f"{selected_sample} sample article loaded!")

article = st.text_area(
    "Enter your article or document",
    key="article_input",
    height=230,
    placeholder="Paste your article here or upload a document..."
)

col1, col2 = st.columns([2, 1])

with col1:
    summary_length = st.selectbox(
        "Select summary length",
        ["Short", "Medium", "Long"],
        index=1
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button(
        "✦ Generate AI Summary",
        use_container_width=True
    )


# ---------------------------------------
# SUMMARY GENERATION
# ---------------------------------------

if generate:

    if not article.strip():
        st.warning("Please enter some text before generating a summary.")

    elif len(article.split()) < 10:
        st.warning("Please enter at least 10 words for better summarization.")

    else:
        with st.spinner(
            "BART is analyzing your text and generating a summary..."
        ):
            try:
                summary = summarize_text(article, summary_length)

                st.session_state.latest_summary = summary
                st.session_state.latest_article = article
                st.session_state.latest_length = summary_length

                save_to_history(
                    article,
                    summary,
                    summary_length
                )

                st.success(
                    "Summary generated and saved to Summary History!"
                )

            except Exception as e:
                st.error(f"Unable to generate summary: {e}")


# ---------------------------------------
# RESULTS
# ---------------------------------------

if st.session_state.get("latest_summary"):

    summary = st.session_state.latest_summary
    original = st.session_state.get("latest_article", "")

    original_words = len(original.split())
    summary_words = len(summary.split())

    reduction = 0

    if original_words > 0:
        reduction = (
            (original_words - summary_words)
            / original_words
        ) * 100

    st.write("")

    # ---------------------------------------
    # ADVANCED TEXT STATISTICS
    # ---------------------------------------

    import re

    original_sentences = len(
        [s for s in re.split(r'[.!?]+', original) if s.strip()]
    )

    original_paragraphs = len(
        [p for p in original.split("\n") if p.strip()]
    )

    original_characters = len(original)

    summary_sentences = len(
        [s for s in re.split(r'[.!?]+', summary) if s.strip()]
    )

    summary_characters = len(summary)

    st.write("")
    st.markdown("## 📈 Advanced Text Statistics")

    st.caption("Detailed analysis of your original article and generated summary.")

    stat1, stat2, stat3 = st.columns(3)

    with stat1:
        st.metric("Original Sentences", original_sentences)

    with stat2:
        st.metric("Original Paragraphs", original_paragraphs)

    with stat3:
        st.metric("Original Characters", original_characters)

    stat4, stat5, stat6 = st.columns(3)

    with stat4:
        st.metric("Summary Sentences", summary_sentences)

    with stat5:
        st.metric("Summary Characters", summary_characters)

    with stat6:
        st.metric("Words Saved", max(0, original_words - summary_words))

    st.markdown("## Generated Summary")

    st.markdown("""
    <div class="result-card">
        <div class="result-title">✦ AI-GENERATED INSIGHTS</div>
    </div>
    """, unsafe_allow_html=True)

    safe_summary = html.escape(summary)

    st.markdown(
        f'<div class="result-text">{safe_summary}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Original Words", original_words)

    with m2:
        st.metric("Summary Words", summary_words)

    with m3:
        st.metric("Text Reduction", f"{reduction:.1f}%")

    # ---------------------------------------
    # SUMMARY COMPARISON
    # ---------------------------------------

    st.write("")
    st.markdown("## 📊 Summary Comparison")
    st.caption("Compare your original content with the AI-generated summary.")

    compare1, compare2 = st.columns(2)

    with compare1:
        st.markdown("### Original Article")
        st.markdown(
            """
            <div style="
                background: white;
                border: 1px solid #E5EBF1;
                border-radius: 12px;
                padding: 18px;
                min-height: 180px;
                color: #172B4D;
                line-height: 1.7;
                white-space: pre-wrap;
                overflow-wrap: anywhere;
            ">
            """ + html.escape(original) + """
            </div>
            """,
            unsafe_allow_html=True
        )

    with compare2:
        st.markdown("### AI-Generated Summary")
        st.markdown(
            """
            <div style="
                background: #E8F5F4;
                border: 1px solid #C7E8E4;
                border-radius: 12px;
                padding: 18px;
                min-height: 180px;
                color: #12344A;
                line-height: 1.7;
                white-space: pre-wrap;
                overflow-wrap: anywhere;
            ">
            """ + html.escape(summary) + """
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.info(
        f"The AI reduced the original content from "
        f"{original_words} words to {summary_words} words, "
        f"a reduction of {reduction:.1f}%."
    )

    st.code(summary, language=None)



    st.download_button(
        "⬇ Download Summary",
        data=summary,
        file_name="synopsis_ai_summary.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    pdf_data = create_summary_pdf(
        summary,
        original_words,
        summary_words,
        reduction
    )

    st.download_button(
        "📄 Download Summary as PDF",
        data=pdf_data,
        file_name="synopsis_ai_summary.pdf",
        mime="application/pdf",
        use_container_width=True
    )


st.markdown("---")

st.caption(
    "SYNOPSIS AI | Powered by DistilBART, Transformers and PyTorch"
)
