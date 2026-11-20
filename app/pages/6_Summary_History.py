
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
HISTORY_FILE = ROOT / "dataset" / "summary_history.json"

st.set_page_config(
    page_title="Summary History | SYNOPSIS AI",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #F5F7FA;
}
.block-container {
    max-width: 1350px;
    padding-top: 2rem;
}
.history-hero {
    background: linear-gradient(120deg, #102A43, #176B78);
    padding: 30px 34px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
}
.history-hero h1 {
    color: white;
    font-size: 32px;
    margin-bottom: 8px;
}
.history-hero p {
    color: #DCE8EE;
    font-size: 15px;
}
.history-card {
    background: white;
    border: 1px solid #E4EAF0;
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 15px;
}
.history-card h4 {
    color: #102A43;
}
.history-muted {
    color: #718096;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


def load_history():
    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


st.markdown("""
<div class="history-hero">
    <h1>📚 Summary History</h1>
    <p>Access and manage your previously generated AI summaries.</p>
</div>
""", unsafe_allow_html=True)

history = load_history()
# Export summary history as CSV
import pandas as pd

if history:
    history_df = pd.DataFrame(history)

    csv_data = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download History as CSV",
        data=csv_data,
        file_name="synopsis_ai_summary_history.csv",
        mime="text/csv",
        use_container_width=True
    )
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Your Saved Summaries")
    st.caption("Your summary records will appear here.")

with col2:
    st.metric("Total Summaries", len(history))

st.divider()

if not history:
    st.info(
        "No summary history found yet. Generate a summary on the "
        "AI Summarizer page to see it here."
    )

else:
    if st.button("🗑️ Clear All History", type="secondary"):
        save_history([])
        st.success("All history has been cleared.")
        st.rerun()

    for index, item in enumerate(reversed(history)):
        original = item.get("original", "")
        summary = item.get("summary", "")
        date = item.get("date", "Date unavailable")
        length = item.get("length", "Medium")

        with st.container(border=True):
            st.markdown(f"### Summary {len(history) - index}")
            st.caption(f"📅 {date}  |  Summary length: {length}")

            with st.expander("View Original Text"):
                st.write(original if original else "No original text saved.")

            st.markdown("**Generated Summary**")
            st.write(summary if summary else "No summary available.")

            st.caption(
                f"Original words: {len(original.split())}  |  "
                f"Summary words: {len(summary.split())}"
            )

            if st.button(
                "Delete This Summary",
                key=f"delete_{index}"
            ):
                del history[len(history) - 1 - index]
                save_history(history)
                st.success("Summary deleted.")
                st.rerun()

st.divider()

st.caption("SYNOPSIS AI | AI-Powered Abstractive Text Summarization")
