# 📡 Telecom RAG Chatbot

An AI-powered Telecom Customer Support Chatbot built using **Retrieval-Augmented Generation (RAG)**. The chatbot answers customer queries by retrieving relevant information from multiple knowledge sources, including FAQs, resolved support tickets, and a telecom user guide.

This project was developed as part of my Generative AI learning journey by following the **Codebasics Agentic AI Crash Course**. I further enhanced the project by implementing additional features such as source citations, confidence-based fallback logic, retrieval evaluation, and a polished Streamlit interface.

---

## 🚀 Features

- 🤖 AI-powered telecom customer support chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 🔎 Semantic search using ChromaDB
- 📄 Multi-source knowledge retrieval:
  - FAQ Database
  - Resolved Support Tickets
  - Telecom User Guide (PDF)
- 📖 Source citations in every response
- ⚠️ Confidence-based fallback for low-confidence queries
- 📊 Retrieval evaluation using Recall@3
- 💬 Interactive Streamlit web application
- ⚡ Fast inference using Groq-hosted Qwen3-32B

---

## 🏗️ Project Architecture

```text
                User Query
                     │
                     ▼
           Streamlit Web Interface
                     │
                     ▼
             Query Embedding
                     │
                     ▼
         Chroma Vector Database
      ┌──────────┬──────────┬──────────┐
      │          │          │
      ▼          ▼          ▼
    FAQs      Tickets     PDF Guide
      │          │          │
      └──────────┴──────────┘
                     │
             Retrieved Context
                     │
                     ▼
            Qwen3-32B (Groq)
                     │
                     ▼
        Response with Source Citations
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Sentence Transformers
- Groq API
- Qwen3-32B
- Pandas
- SQLite

---

## 📂 Knowledge Sources

The chatbot retrieves information from three different sources:

- 📄 FAQ Dataset (CSV)
- 🎫 Resolved Support Tickets (SQLite)
- 📘 Telecom User Guide (PDF)

All documents are embedded using **Sentence Transformers** and stored in **ChromaDB** for semantic retrieval.

---

## ✨ Additional Enhancements Implemented

### ✅ Source Citations

Every response includes references to the retrieved source(s), such as:

- FAQ ID
- Ticket ID
- Guide Page

---

### ✅ Confidence-Based Fallback

Implemented similarity score checking using ChromaDB.

If no retrieved document exceeds the confidence threshold, the chatbot returns a fallback response instead of generating an unsupported answer.

---

### ✅ Retrieval Evaluation

Developed a retrieval evaluation script using **10 handcrafted telecom queries** to measure **Recall@3**.

**Result**

```text
Recall@3 = 10/10 (100%)
```

---

### ✅ User Interface Improvements

- Interactive Streamlit dashboard
- Sample question sidebar
- Conversation history
- Response streaming
- Loading indicator
- Clean and responsive UI

---

## 📷 Demo


Example:


images\Screenshot (51).png
images\Screenshot (52).png

---
## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/TechieMoksha/telecom-rag-chatbot
cd telecom-rag-chatbot
```

### Install dependencies

```bash
uv sync
```

### Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

### Run the application

```bash
uv run streamlit run app.py
```

## 🙏 Acknowledgements

This project was built while following the **Agentic AI Crash Course** by **Dhaval Patel** from **Codebasics**.

I sincerely thank **Dhaval Patel** and the **Codebasics** team for creating practical, hands-on learning content on Generative AI and Agentic AI.

In addition to the course project, I independently implemented the following enhancements:

- Source citations
- Confidence-based retrieval fallback
- Retrieval evaluation (Recall@3)
- Streamlit UI improvements

---

## 👩‍💻 Author

**Mokshada Patil**

B.Tech in Data Science

Passionate about Data Analytics, Machine Learning, Deep Learning, Generative AI, and Agentic AI.

- 💼 LinkedIn: https://www.linkedin.com/in/mokshada-patil-80132b2b0/
- 💻 GitHub: https://github.com/TechieMoksha

---

⭐ If you found this project interesting, feel free to star the repository!