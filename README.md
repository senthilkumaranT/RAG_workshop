# RAG (Retrieval-Augmented Generation)

This folder contains scripts and resources for a Retrieval-Augmented Generation (RAG) pipeline using LangChain, Ollama, and Qdrant. The pipeline enables document ingestion, semantic search, and LLM-based summarization.

## Contents

- `retriever.py`: Command-line tool to query a Qdrant vector database using semantic search and summarize results with an LLM.
- `llm.py`: Utility for interacting with an Ollama LLM (Llama 3.2 1B) to generate summaries.
- `upload.py`: Script to ingest and embed PDF documents into a Qdrant vector store.
- `give me detail explantion pdf of perplexity.pdf`, `MOR.pdf`: Example PDF files for testing document ingestion and retrieval.

## Setup

1. **Dependencies**: Install required Python packages:
   - `langchain_ollama`
   - `langchain_qdrant`
   - `langchain_community`
   - `litellm`

2. **Ollama LLM**: Ensure Ollama is running locally and accessible at `http://localhost:11434`.

3. **Qdrant**: The scripts are configured to use a remote Qdrant instance. Update the `url` and `api_key` in the scripts if needed.

## Usage

### 1. Ingest a PDF into Qdrant

Edit `upload.py` to set your PDF file path, then run:
```bash
python upload.py
```
This will embed the PDF and upload it to the Qdrant collection `my_documents`.

### 2. Query and Summarize

Run `retriever.py` and enter your question at the prompt:
```bash
python retriever.py
```
The script will search for relevant document chunks and summarize them using the LLM.

## Notes
- The included PDFs are for demonstration. You can replace them with your own documents.
- API keys and URLs are hardcoded for demonstration; update them for production use.

