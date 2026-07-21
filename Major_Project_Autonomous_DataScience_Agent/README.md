# 🤖 Autonomous Data Science Agent

A Multi-Agent AI system that automates data analysis, visualization, Python code generation, execution, and self-healing error correction using Large Language Models (LLMs).

---

## 📖 Project Overview

Autonomous Data Science Agent is an AI-powered application that assists users in analyzing datasets through multiple specialized AI agents.

The system performs:

- Automated dataset profiling
- Data cleaning
- Visualization
- AI-powered dataset analysis
- Python code generation
- Code execution
- Automatic error detection and correction

The application is built using Streamlit, Pandas, LangChain, and Groq LLM.

## ✨ Features

- 📂 Upload CSV, Excel, and JSON datasets
- 📊 Automatic data profiling
- 🧹 Intelligent data cleaning
- 📈 Interactive visualizations
- 🤖 AI-powered dataset analysis
- 💻 AI-generated Python code
- ▶ Execute generated code
- 🔧 Self-healing AI that fixes execution errors automatically

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- LangChain
- Groq LLM
- python-dotenv


## Setup

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

4. Run the application

```bash
streamlit run app.py
```