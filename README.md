# Agentic RAG System

This project is a **User-Facing Chat-style Agentic Retrieval-Augmented Generation (RAG) System** powered by Google's **Gemini** LLM. It enables users to interact with a chat agent that fetches real-time information from a continuously updated local data pipeline, offering accurate and up-to-date answers.

---

## Features

- ✅ FastAPI-based backend for async communication
- ✅ Gemini Pro integration (via Vertex AI / PaLM API)
- ✅ Daily asynchronous pipeline to fetch, process, and store data in **MySQL**
- ✅ Chat UI for natural language querying
- ✅ Tool calling capability to use custom tools (e.g., search, summary)
- ✅ Local LLM hosting optional (via Ollama or LangChain)

---

## Project Structure

```bash
agentic_rag/
├── agent/
│   └── agent_handler.py         # Gemini API calls and agent logic
├── api/
│   └── main.py                  # FastAPI app with /query endpoint
├── data/
│   └── pipeline.py              # Async daily pipeline to fetch & store data
├── database/
│   └── mysql_utils.py           # MySQL setup and data operations
├── static/
│   └── index.html               # Minimal chat UI
├── .env                         # Environment variables (API keys, DB URL)
└── requirements.txt             # Python dependencies
```
##How It Works
- Daily Pipeline pulls external data (e.g., news, documents, records) and stores them in MySQL.
- User queries are received via the FastAPI /query endpoint.
- A Gemini-based agent processes the query using:
- Search/summarize tools
- The knowledge stored from recent pipeline data
- The response is returned and displayed via the chat UI.

##Setup
```bash
git clone https://github.com/RohithKesoju/agentic_rag.git
cd agentic_rag
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```
##Run the App
```bash
uvicorn api.main:app --reload
```

##Results
![Output1](https://github.com/user-attachments/assets/50e2c030-aed4-4f6e-9ff7-6e01c25df8ad)

![Output2](https://github.com/user-attachments/assets/793a968e-9a01-41da-a833-dbefea2d7a0e)

![MySQL](https://github.com/user-attachments/assets/1c570367-53c5-4575-bede-582be7cccfef)

