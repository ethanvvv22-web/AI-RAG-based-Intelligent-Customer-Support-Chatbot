# 🤖 AI Customer Support Chatbot (RAG + ReAct Agent)

An intelligent customer support system for robotic vacuum cleaners, powered by Retrieval-Augmented Generation (RAG) and a ReAct-based agent with tool-calling capabilities.

## 🚀 Key Features

- 🔍 RAG-based knowledge retrieval for accurate, context-aware answers
- 🧠 ReAct Agent for multi-step reasoning and dynamic tool selection
- 🛠️ Tool-calling system (RAG, weather, user data, etc.)
- ⚡ Real-time streaming response
- 🎯 Designed for real-world robotic vacuum usage scenarios


## 🏗️ System Architecture

User Query → Agent → Tool Selection → RAG Retrieval → LLM → Final Answer

### Components:

- **Frontend**: User interface for interaction
- **Agent (LangChain)**: Decides which tool to use
- **RAG Pipeline**:
  - Embedding model
  - Vector database (Chroma)
  - Top-K retrieval
- **LLM**: Generates final answer
- **Tools**:
  - RAG summarization
  - Weather API
  - User data API


## 🔄 How It Works

1. User submits a query
2. The agent analyzes intent
3. The agent selects the appropriate tool
4. If needed, RAG retrieves relevant knowledge
5. The LLM generates a response based on context
6. Final answer is returned to the user

## 🧰 Tech Stack

- Python
- LangChain
- Chroma (Vector Database)
- OpenAI / LLM API
- Embeddings
- Flask (or FastAPI)
- Docker (optional)

## 🖥️ Demo

Below is a screenshot of the system interface:
<img width="844" height="416" alt="image" src="https://github.com/user-attachments/assets/ab67caed-26ef-49e7-b67d-fc67fbd566c4" />

The system allows users to ask questions about robotic vacuum cleaners, and the agent will:
- Understand user intent
- Retrieve relevant knowledge using RAG
- Generate accurate responses using LLM
