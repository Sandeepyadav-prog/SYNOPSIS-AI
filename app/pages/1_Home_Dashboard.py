
import streamlit as st

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.markdown("""
<style>

/* MAIN APPLICATION */
.stApp {
    background: #F5F7FA;
    color: #172B4D;
}

.block-container {
    max-width: 1350px;
    padding: 1.5rem 2.5rem 2rem 2.5rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #102A43;
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

/* HEADINGS */
h1 {
    color: #102A43;
    font-size: 30px !important;
    font-weight: 750 !important;
}

h2 {
    color: #102A43;
    font-size: 21px !important;
}

h3 {
    color: #176B78;
    font-size: 17px !important;
}

/* HERO */
.hero {
    background: linear-gradient(115deg, #102A43, #176B78);
    padding: 30px 34px;
    border-radius: 16px;
    color: white;
    margin-bottom: 26px;
}

.hero-tag {
    color: #83E4D4;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.hero-title {
    color: white;
    font-size: 32px;
    font-weight: 750;
    margin-bottom: 10px;
}

.hero-description {
    color: #DCEAF0;
    font-size: 14px;
    line-height: 1.7;
    max-width: 650px;
}

/* METRIC CARDS */
.metric-card {
    background: white;
    border: 1px solid #E5EBF1;
    border-radius: 13px;
    padding: 19px;
    min-height: 105px;
    box-shadow: 0 3px 12px rgba(16,42,67,0.035);
}

.metric-label {
    color: #718096;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

.metric-number {
    color: #102A43;
    font-size: 21px;
    font-weight: 750;
    margin-top: 10px;
}

/* FEATURE CARDS */
.feature-card {
    background: white;
    border: 1px solid #E5EBF1;
    border-radius: 13px;
    padding: 21px;
    min-height: 145px;
    box-shadow: 0 3px 12px rgba(16,42,67,0.035);
    transition: 0.2s ease;
}

.feature-icon {
    font-size: 23px;
    margin-bottom: 12px;
}

.feature-title {
    color: #102A43;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 8px;
}

.feature-description {
    color: #718096;
    font-size: 12px;
    line-height: 1.7;
}

/* INFO STRIP */
.info-strip {
    background: #E8F5F4;
    border-left: 4px solid #159A91;
    padding: 15px 18px;
    border-radius: 8px;
    color: #245B61;
    font-size: 13px;
    margin-top: 10px;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 11px;
    padding: 28px 0 5px 0;
}

/* BUTTONS */
.stButton > button {
    background: #147D79;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 9px 18px;
    font-weight: 600;
}

.stButton > button:hover {
    background: #10645F;
    color: white;
}

/* REMOVE EXCESS TOP SPACE */
header[data-testid="stHeader"] {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------
# HERO SECTION
# ---------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">AI-POWERED TEXT INTELLIGENCE PLATFORM</div>
    <div class="hero-title">Welcome to SYNOPSIS AI ✦</div>
    <div class="hero-description">
        Transform lengthy documents into meaningful, concise insights.
        Experience intelligent abstractive text summarization powered
        by advanced Transformer technology.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------
# PLATFORM OVERVIEW
# ---------------------------------------

st.markdown("## Platform Overview")

st.caption("An intelligent summarization platform powered by DistilBART.")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">AI MODEL</div>
        <div class="metric-number">DistilBART</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">AI TECHNOLOGY</div>
        <div class="metric-number">Transformer</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">CORE APPLICATION</div>
        <div class="metric-number">Abstractive AI</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------
# FEATURES
# ---------------------------------------

st.write("")
st.markdown("## Explore the Platform")
st.caption("Discover the tools and capabilities available in SYNOPSIS AI.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">✦</div>
        <div class="feature-title">AI Text Summarization</div>
        <div class="feature-description">
            Convert lengthy articles and documents into short,
            meaningful summaries with adjustable summary lengths.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Model Performance</div>
        <div class="feature-description">
            Explore model architecture, evaluation methodology
            and ROUGE-based summarization performance.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚙️</div>
        <div class="feature-title">AI Workflow</div>
        <div class="feature-description">
            Understand the complete pipeline, including dataset
            preparation, text preprocessing and Transformer inference.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎓</div>
        <div class="feature-title">Project Information</div>
        <div class="feature-description">
            Explore project objectives, technologies, applications
            and the role of abstractive summarization.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------
# INFORMATION STRIP
# ---------------------------------------

st.write("")

st.markdown("""
<div class="info-strip">
    <b>Did you know?</b><br>
    DistilBART is a distilled Transformer model designed to provide
    efficient text summarization while retaining important information.
</div>
""", unsafe_allow_html=True)


# ---------------------------------------
# FOOTER
# ---------------------------------------

st.markdown("""
<div class="footer">
    SYNOPSIS AI &nbsp; | &nbsp;
    Intelligent Text Summarization Platform<br>
    Built with Python, Streamlit and Transformer Technology
</div>
""", unsafe_allow_html=True)
