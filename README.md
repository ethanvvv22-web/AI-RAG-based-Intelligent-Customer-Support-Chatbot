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

### 📌 RAG-Based Recommendation Result

This example shows how the system retrieves relevant knowledge using the RAG pipeline and generates a structured recommendation based on user requirements.

<img width="1134" height="154" alt="image" src="https://github.com/user-attachments/assets/078e8470-a20c-48c5-a0c7-011081be356c" />

<img width="1257" height="765" alt="image" src="https://github.com/user-attachments/assets/59e3a0e3-a0b0-48a0-9255-3f3474c4cffd" />


### 📊 Usage Report Generation

The system supports generating personalized monthly usage reports for robotic vacuum users.

It follows a structured tool-calling workflow:

1. Retrieve user ID  
2. Get the current or specified month  
3. Inject report context  
4. Fetch external usage data  
5. Generate a summarized report using the LLM  

#### 🔄 Workflow

User Request → Agent → Tool Chain → Report Generation

#### 🛠️ Tools Involved

- `get_user_id`: Retrieve user identity  
- `get_current_month`: Determine report period  
- `fill_context_for_report`: Prepare report context  
- `fetch_external_data`: Fetch usage data
  
#### 💬 Example
<img src="https://github.com/user-attachments/assets/fa8da915-2f0d-4b59-ac7d-102f11721df4" width="600" />

<img src="https://github.com/user-attachments/assets/ef26d25b-6e59-4b47-b7d8-c0e0f73ce78d" width="600" />

<img src="https://github.com/user-attachments/assets/49817837-fdf8-423b-ac20-cb6cffd1bdbe" width="600" />

<img src="https://github.com/user-attachments/assets/6dc733c5-a40e-48f4-bdb0-d8fc499c6cf7" width="600" />

