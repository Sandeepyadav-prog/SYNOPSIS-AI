
# ✦ SYNOPSIS AI
### AI-Powered Abstractive Text Summarization

SYNOPSIS AI is an intelligent text summarization application that uses Natural Language Processing (NLP) and a pretrained Transformer model to generate concise, meaningful summaries from lengthy text documents.

The application supports TXT, PDF, and DOCX uploads, adjustable summary lengths, summary history, and downloadable summaries.

## 🚀 Key Features

- **AI Summarization:** Generates human-readable abstractive summaries.
- **Multiple File Formats:** Supports TXT, PDF, and DOCX uploads.
- **Adjustable Summary Length:** Short, Medium, and Long options.
- **Sample Article Library:** Preloaded sample articles for testing.
- **Advanced Text Statistics:** Displays word, sentence, and character statistics.
- **Summary History:** Stores previously generated summaries.
- **CSV Export:** Download summary history as a CSV file.
- **PDF Export:** Download generated summaries as PDF files.
- **TXT Export:** Download summaries as text files.
- **Model Evaluation:** ROUGE-1, ROUGE-2, and ROUGE-L evaluation metrics.
- **Modern Dashboard:** Interactive Streamlit interface.

## 🧠 Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / Interface | Streamlit |
| AI / NLP | Hugging Face Transformers |
| Model | DistilBART |
| Deep Learning | PyTorch |
| Data Processing | Pandas, NumPy |
| PDF Processing | PyPDF |
| DOCX Processing | python-docx |
| PDF Generation | ReportLab |
| Evaluation | ROUGE |
| Dataset | CNN/DailyMail |

## 🤖 AI Model

**Model:** `sshleifer/distilbart-cnn-12-6`

SYNOPSIS AI uses a pretrained DistilBART sequence-to-sequence Transformer model for abstractive text summarization.

The model generates summaries by understanding the context and meaning of the input text rather than simply extracting sentences.

## 📂 Project Structure

```text
Abstractive_Text_Summarization/
│
├── app/
│   ├── streamlit_app.py
│   └── pages/
│       ├── 1_Home_Dashboard.py
│       ├── 2_AI_Summarizer.py
│       ├── 3_Model_Insights.py
│       ├── 4_How_It_Works.py
│       ├── 5_About_Project.py
│       └── 6_Summary_History.py
│
├── dataset/
│   ├── cnn_dailymail_sample.csv
│   ├── processed_cnn_dailymail.csv
│   ├── rouge_evaluation_results.csv
│   └── summary_history.json
│
├── notebooks/
├── models/
├── docs/
├── utils/
│   └── summarizer.py
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Abstractive_Text_Summarization
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Application

```bash
python -m streamlit run app/streamlit_app.py
```

The application will open in your browser.

## 📊 Model Evaluation

The model is evaluated using ROUGE metrics:

- **ROUGE-1:** Measures unigram overlap.
- **ROUGE-2:** Measures bigram overlap.
- **ROUGE-L:** Measures the longest common subsequence.

Evaluation results are displayed on the Model Insights dashboard.

## 🔄 Application Workflow

1. Upload a document or enter text.
2. Extract the document content.
3. Select the desired summary length.
4. Generate an AI-powered summary.
5. View the generated summary and text statistics.
6. Download the summary or access it later through Summary History.

## 🎯 Project Objectives

- Reduce the time required to read lengthy documents.
- Generate concise and meaningful summaries.
- Apply Transformer-based NLP techniques.
- Provide an easy-to-use document summarization interface.
- Evaluate summarization performance using ROUGE metrics.

## 🔮 Future Enhancements

- Multilingual text summarization.
- Real-time summarization of web articles.
- Improved summarization for very long documents.
- User authentication and personalized history.
- Cloud-based model optimization.

## 👩‍💻 Project Information

**Project Name:** SYNOPSIS AI  
**Project Domain:** Artificial Intelligence and Natural Language Processing  
**Project Type:** Academic Project

---

*Built with Python, NLP, Transformers, and Streamlit.*
