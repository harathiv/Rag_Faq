# Python FAQ Assistant — Traditional RAG

## 1. Project Overview

The Python FAQ Assistant is a Retrieval-Augmented Generation (RAG) application that answers user questions using information retrieved from Python FAQ documentation.

The application combines **MinSearch for information retrieval** and **Ollama for local language model generation**. Instead of relying only on the language model's existing knowledge, it retrieves relevant FAQ content and uses that content to generate an answer.

This project demonstrates the basic workflow of building a traditional RAG application.

## 2. How Does It Work?

The application follows these steps:

1. **Collect documents:** Fetch Python FAQ documentation from the official Python GitHub repository.
2. **Extract questions and answers:** Parse the documentation into question-and-answer pairs.
3. **Clean the data:** Organize the extracted information into a consistent format.
4. **Save the data:** Store the processed FAQ documents in a JSON file.
5. **Build the search index:** Use MinSearch to index the questions and answers so relevant information can be retrieved.
6. **Retrieve relevant information:** When a user asks a question, search the FAQ index for relevant documents.
7. **Generate an answer:** Pass the retrieved information and the user's question to a locally running Ollama language model.
8. **Display the response:** Show the generated answer in the terminal.

## 3. Technologies Used

- **Python:** Implements the application logic.
- **MinSearch:** Retrieves relevant FAQ documents using keyword-based search.
- **Ollama:** Runs the language model locally and generates responses.
- **Requests:** Fetches documentation from GitHub.
- **JSON:** Stores the processed FAQ data.
- **python-dotenv:** Supports loading environment variables when needed.

## 4. Project Structure

```text
raq_faq/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    └── faqs.json
```

- `app.py` — Loads the FAQ data, creates the search index, retrieves relevant documents, and generates answers.
- `requirements.txt` — Lists the Python packages required by the application.
- `README.md` — Documents the project and explains how to run it.
- `.gitignore` — Excludes virtual environments, secret files, and unnecessary generated files from Git.
- `data/faqs.json` — Contains the processed FAQ questions and answers used by the application.

## 5. Installation and Setup

### Prerequisites

Before running the application, install:

- Python
- Git (optional, for cloning the repository)
- Ollama
- A language model supported by Ollama

Make sure Ollama is running and the model configured in `app.py` is installed locally.

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd raq_faq
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual URL of your GitHub repository.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure Ollama

Install Ollama and download a model compatible with your computer.

For example, if you choose a model named `MODEL_NAME`, download it using:

```bash
ollama pull MODEL_NAME
```

Make sure the model name in `app.py` matches the model you installed. Replace `MODEL_NAME` with the actual model name.

### Step 5: Run the application

From the project folder, run:

```bash
python app.py
```

Type a question when prompted. Enter `exit` to quit the application.

## 6. Example Usage

**User question:**

```text
What is Python?
```

**Application workflow:**

1. Searches the FAQ index for relevant documents.
2. Selects relevant FAQ content.
3. Sends the question and retrieved content to the Ollama model.
4. Displays the generated response.

The quality of the answer depends on the available FAQ content, retrieval results, and the language model.

## 7. Key Concepts Learned

Through this project, I explored:

- Document collection and text processing.
- Extracting and storing structured FAQ data.
- Keyword-based information retrieval.
- Building a searchable document index.
- Connecting a language model to a retrieval pipeline.
- Using a local LLM through Ollama.
- Organizing a Python application into reusable components.
- Managing project dependencies and preparing a project for GitHub.

## 8. Current Limitations

- The FAQ dataset covers only the documentation collected and processed for this project.
- The document parser may not extract every question and answer perfectly.
- MinSearch uses keyword-based retrieval rather than semantic vector embeddings.
- Answer quality depends on the retrieved context and the language model.
- The application runs as a terminal-based assistant rather than a web application.

## 9. Future Improvements

- Improve document parsing and FAQ coverage.
- Add semantic retrieval using embeddings and a vector database.
- Evaluate retrieval quality and answer accuracy.
- Add a web interface using Streamlit.
- Improve handling of questions that are not covered by the available documents.

## 10. Learning Project

This project was built as a hands-on learning exercise to understand how a traditional RAG pipeline connects document processing, retrieval, and language model generation.

The goal is to develop a practical understanding of RAG fundamentals and gradually improve the application.
