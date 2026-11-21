# ✨ SYNOPSIS AI
### AI-Powered Abstractive Text Summarization

<p align="center">
  <strong>Transform lengthy documents into concise, meaningful summaries using Artificial Intelligence.</strong>
</p>

## 🌐 Live Demo

🚀 **Try SYNOPSIS AI:**  
[https://synopsis-ai-up8o4cafxreugohdgkwszu.streamlit.app/](https://synopsis-ai-up8o4cafxreugohdgkwszu.streamlit.app/)

**GitHub Repository:**  
[https://github.com/Sandeepyadav-prog/SYNOPSIS-AI](https://github.com/Sandeepyadav-prog/SYNOPSIS-AI)

---

## 📌 Project Overview

SYNOPSIS AI is an AI-powered abstractive text summarization application developed using Natural Language Processing (NLP) and Transformer-based deep learning techniques.

It uses a pretrained DistilBART model to understand lengthy text and generate shorter, meaningful, human-readable summaries while preserving the important information.

The application provides an interactive web interface where users can enter text, upload documents, select summary length, generate summaries, and download their results.

## 🚀 Key Features

- **AI-Powered Summarization:** Generates meaningful abstractive summaries using DistilBART.
- **Multiple File Uploads:** Supports TXT, PDF, and DOCX documents.
- **Adjustable Summary Length:** Choose Short, Medium, or Long summaries.
- **Sample Articles Library:** Includes sample articles for quick testing.
- **Advanced Text Statistics:** Displays word, sentence, and character statistics.
- **Summary History:** Stores previously generated summaries.
- **CSV Export:** Download summary history in CSV format.
- **PDF Export:** Download generated summaries as PDF files.
- **TXT Export:** Download summaries as text files.
- **Model Evaluation:** Uses ROUGE-1, ROUGE-2, and ROUGE-L metrics.
- **Interactive Dashboard:** Modern, user-friendly Streamlit interface.
- **Multiple Application Pages:** Includes dashboard, summarizer, model insights, workflow, project information, and summary history.

## 🧠 Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / Interface | Streamlit |
| Artificial Intelligence | Hugging Face Transformers |
| NLP Model | DistilBART |
| Deep Learning Framework | PyTorch |
| Data Processing | Pandas, NumPy |
| Dataset | CNN/DailyMail |
| PDF Reading | PyPDF |
| DOCX Processing | python-docx |
| PDF Generation | ReportLab |
| Model Evaluation | ROUGE |
| Data Visualization | Matplotlib, Seaborn |
| Development Environment | VS Code |

## 🤖 AI Model

**Model Name:** `sshleifer/distilbart-cnn-12-6`

SYNOPSIS AI uses a pretrained DistilBART sequence-to-sequence Transformer model for abstractive text summarization.

Unlike extractive summarization, which selects existing sentences from the original text, abstractive summarization generates new sentences while preserving the main meaning and context.

The model is based on the BART architecture and is designed for summarization tasks.

## 📊 Dataset

The project uses a sample of the **CNN/DailyMail dataset**, which contains news articles and their corresponding human-written summaries.

The dataset is used for:
- Text analysis and exploration.
- Data preprocessing.
- Understanding article and summary lengths.
- Testing the summarization model.
- Evaluating summarization performance.

## 📂 Project Structure

```text
SYNOPSIS-AI/
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
│   ├── summary_history.json
│   ├── article_length_distribution.png
│   └── summary_length_distribution.png
│
├── notebooks/
│   ├── 01_download_dataset.py
│   ├── 02_eda.py
│   ├── 03_text_preprocessing.py
│   ├── 04_test_summarizer.py
│   ├── 05_model_evaluation.py
│   └── 06_test_bart.py
│
├── utils/
│   └── summarizer.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run SYNOPSIS AI locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Sandeepyadav-prog/SYNOPSIS-AI.git
```

### 2. Navigate to the Project Folder

```bash
cd SYNOPSIS-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

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

The application will open in your default web browser.

## 🔄 Application Workflow

1. Open the SYNOPSIS AI web application.
2. Navigate to the AI Summarizer page.
3. Enter text or upload a TXT, PDF, or DOCX document.
4. Select the desired summary length.
5. Click the Generate AI Summary button.
6. View the generated summary and text statistics.
7. Download the summary as a TXT or PDF file.
8. Access previously generated summaries through Summary History.

## 📈 Model Evaluation

The summarization model is evaluated using ROUGE metrics.

| Metric | Description |
|---|---|
| ROUGE-1 | Measures unigram overlap between generated and reference summaries. |
| ROUGE-2 | Measures bigram overlap. |
| ROUGE-L | Measures the longest common subsequence. |

Evaluation results are displayed on the Model Insights dashboard.

## 🎯 Project Objectives

- Develop an AI-based abstractive text summarization system.
- Reduce the time required to understand lengthy documents.
- Generate concise and meaningful summaries.
- Apply Transformer-based NLP techniques.
- Provide support for multiple document formats.
- Evaluate summarization performance using ROUGE metrics.
- Develop an interactive and accessible web application.

## 🔮 Future Enhancements

- Multilingual text summarization.
- Real-time summarization of web articles.
- Improved summarization of very long documents.
- User authentication and personalized history.
- Cloud-based model optimization.
- Additional summarization models for comparison.

## 👩‍💻 Project Information

| Detail | Information |
|---|---|
| Project Name | SYNOPSIS AI |
| Project Domain | Artificial Intelligence and Natural Language Processing |
| Project Type | Academic Project |
| Programming Language | Python |
| Model | DistilBART |
| Deployment | Streamlit Community Cloud |

---

<p align="center">
  <strong>✨ SYNOPSIS AI — Turning Long Text into Clear Insights.</strong>
  <br>
  Built with Python, NLP, Transformers, PyTorch, and Streamlit.
</p>