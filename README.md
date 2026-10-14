# 📡 Telecom RAG Chatbot

An AI-powered telecom customer support chatbot built using **Retrieval-Augmented Generation (RAG)**. It answers customer queries by retrieving relevant information from FAQs, resolved support tickets, and a telecom user guide.

Developed as part of my Generative AI learning journey through the **Codebasics Agentic AI Crash Course**, this project was enhanced with source citations, confidence-based fallback logic, retrieval evaluation, and an interactive Streamlit interface.

## 🚀 Live Demo
<img width="943" height="390" alt="image" src="https://github.com/user-attachments/assets/78d74037-a194-4627-949f-419fcc0a5d61" />

**[Try the Telecom RAG Chatbot →](https://telecom-rag-chatbot-8pqx6z8gfmicgm6tnxc87r.streamlit.app/)**

Explore the chatbot and test it with telecom-related customer support questions.

## ✨ Features

- 🤖 AI-powered telecom customer support
- 📚 Retrieval-Augmented Generation (RAG)
- 🔎 Semantic search using ChromaDB
- 📄 Multi-source knowledge retrieval from FAQs, support tickets, and PDF documentation
- 📖 Source citations in responses
- ⚠️ Confidence-based fallback for low-confidence queries
- 📊 Retrieval evaluation using Recall@3
- 💬 Interactive Streamlit interface
- ⚡ Inference using Groq-hosted Qwen3-32B

## 📸 Application Screenshots

### Chatbot Interface

![Telecom RAG Chatbot - Interface](images/Screenshot%20(51).png)

### Chatbot Response and Source Retrieval

![Telecom RAG Chatbot - Response](images/Screenshot%20(52).png)

## 🏗️ Project Architecture

```text
              User Query
                   |
                   v
         Streamlit Web Interface
                   |
                   v
            Query Embedding
                   |
                   v
        ChromaDB Vector Database
          /        |        \
         v         v         v
       FAQs     Tickets    PDF Guide
          \        |        /
                   |
                   v
           Retrieved Context
                   |
                   v
            Qwen3-32B (Groq)
                   |
                   v
       Response with Source Citations
```

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM Framework:** LangChain
- **Vector Database:** ChromaDB
- **Embeddings:** Hugging Face Sentence Transformers
- **LLM Inference:** Groq API, Qwen3-32B
- **Data Storage:** SQLite, CSV
- **Data Processing:** Pandas

## 📂 Knowledge Sources

The chatbot retrieves information from three knowledge sources:

- 📄 **FAQ Dataset:** CSV-based frequently asked questions
- 🎫 **Resolved Support Tickets:** Historical support data stored in SQLite
- 📘 **Telecom User Guide:** PDF documentation

The knowledge sources are converted into embeddings and stored in ChromaDB to support semantic search and context retrieval.

## 🔧 Additional Enhancements

### Source Citations
Responses include references to retrieved sources, such as FAQ IDs, ticket IDs, and guide page numbers, where applicable.

### Confidence-Based Fallback
Similarity scores are checked to identify low-confidence retrievals. When relevant information cannot be retrieved above the configured threshold, the chatbot returns a fallback response instead of generating an unsupported answer.

### Retrieval Evaluation
A custom evaluation script tests retrieval performance using 10 handcrafted telecom queries.

**Evaluation result:**

```text
Recall@3 = 10/10 (100%)
```

*Note: This result reflects the custom evaluation dataset and is not a guarantee of performance on unseen queries.*

### User Interface Improvements
- Interactive Streamlit interface
- Sample questions in the sidebar
- Conversation history
- Response streaming
- Loading indicators
- Clean, user-friendly layout

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/TechieMoksha/telecom-rag-chatbot.git
cd telecom-rag-chatbot
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your Groq API key.

### 4. Run the application

```bash
uv run streamlit run app.py
```

## 🙏 Acknowledgements

This project was developed while following the **Agentic AI Crash Course** by **Dhaval Patel and the Codebasics team**.

I further enhanced the course project by implementing source citations, confidence-based retrieval fallback, Recall@3 evaluation, and UI improvements.

## 👩‍💻 Author

**Mokshada Patil**  
B.Tech in Data Science

Interested in Data Analytics, Machine Learning, Generative AI, and building practical AI applications.

- 🚀 [Live Project Demo](https://telecom-rag-chatbot-8pqx6z8gfmicgm6tnxc87r.streamlit.app/)

---

⭐ If you find this project interesting, consider starring the repository!
