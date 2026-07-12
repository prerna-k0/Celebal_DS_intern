# 📘 Week 7 – Document Question Answering System using RAG

## Project Overview

This project implements a simple **Retrieval-Augmented Generation (RAG)** system that answers questions based on a custom PDF document.

Instead of relying only on a language model's internal knowledge, the system retrieves relevant information from the uploaded document and provides it as context to a language model. This helps generate answers grounded in the document.

## Objective

The objective of this project is to:

* Understand the concept of Retrieval-Augmented Generation (RAG).
* Process and extract text from custom PDF documents.
* Split document text into smaller overlapping chunks.
* Generate semantic embeddings for text chunks.
* Store and search embeddings using a vector database.
* Retrieve relevant information based on a user query.
* Generate context-based answers using a language model.

## RAG Pipeline

```text
Custom PDF Document
        ↓
   Text Extraction
        ↓
    Text Chunking
        ↓
 Embedding Generation
        ↓
 FAISS Vector Database
        ↓
     User Query
        ↓
 Similarity Search
        ↓
Relevant Text Chunks
        ↓
    FLAN-T5 Model
        ↓
  Generated Answer
```

## Technologies Used

* Python
* PyPDF
* Sentence Transformers
* FAISS
* Hugging Face Transformers
* FLAN-T5
* PyTorch
* Google Colab

## Models Used

### Embedding Model

`all-MiniLM-L6-v2`

The Sentence Transformer model converts document chunks and user queries into 384-dimensional semantic vector embeddings.

### Language Model

`google/flan-t5-base`

FLAN-T5 generates the final answer using the relevant context retrieved from the document.

## Project Workflow

1. Upload a custom PDF document.
2. Extract text from the PDF using PyPDF.
3. Split the extracted text into overlapping chunks.
4. Convert each text chunk into a vector embedding.
5. Store the embeddings in a FAISS vector index.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant document chunks using similarity search.
8. Provide the retrieved context and question to FLAN-T5.
9. Generate a document-grounded answer.

## Results

The system successfully processed the custom PDF document and created a searchable vector database.

* PDF pages processed: **1**
* Total characters extracted: **2750**
* Total text chunks created: **7**
* Embedding dimension: **384**
* Total vectors stored in FAISS: **7**

### Sample Questions

**Question:** What is the educational qualification mentioned?
**Answer:** B.Tech in Computer

**Question:** What internship experience is mentioned?
**Answer:** MERN-stack development

**Question:** What projects are included in the document?
**Answer:** Detecting Fake Banking APKs

**Question:** What programming skills are mentioned?
**Answer:** Java, C, Python, HTML, CSS, JavaScript, Node.js, Express.js, DSA, OOPs, DBMS, CN, MySQL, and MongoDB.

The system also successfully handled a question whose answer was not available in the document.

**Question:** What is the person's favorite movie?
**Answer:** The answer is not available in the document.

## Key Learnings

* Understanding Retrieval-Augmented Generation
* Document ingestion and text extraction
* Text chunking with overlap
* Semantic embeddings
* Vector similarity search
* FAISS vector databases
* Context retrieval
* Language model-based answer generation
* Reducing hallucinations through document grounding

## Future Improvements

* Use larger and multiple PDF documents.
* Implement improved semantic chunking strategies.
* Experiment with different embedding models.
* Add hybrid keyword and vector search.
* Add re-ranking for improved retrieval accuracy.
* Use larger language models for more detailed answers.
* Develop an interactive user interface using Streamlit or Gradio.

## Conclusion

This project demonstrates the implementation of a basic Retrieval-Augmented Generation system for document-based question answering.

By combining semantic retrieval using Sentence Transformers and FAISS with answer generation using FLAN-T5, the system can retrieve relevant information from a custom document and generate context-aware answers.

The project demonstrates the fundamental architecture behind modern AI-powered knowledge assistants, document chatbots, enterprise search systems, and question-answering applications.

## Project Files

```text
Week7_Document_Question_Answering_RAG/
│
├── Week7_Document_Question_Answering_RAG.ipynb
├── README.md
└── requirements.txt
```

## Requirements

```text
pypdf
sentence-transformers
faiss-cpu
transformers
sentencepiece
torch
numpy
```
