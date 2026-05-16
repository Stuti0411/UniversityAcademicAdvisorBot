# 🎓 University Academic Advisor Bot

An AI-powered Academic Advisor Assistant built using Generative AI, RAG (Retrieval-Augmented Generation), SQL Agent, and Web Search Integration.

This chatbot helps students and universities by answering questions from:
- University PDF documents
- Student academic records
- Live internet/web search

---

# 🚀 Features

✅ PDF Question Answering using RAG  
✅ Vector Database using FAISS  
✅ Semantic Search using Sentence Transformers  
✅ SQL Agent for Student Records  
✅ Smart Router for Query Classification  
✅ Live Google Web Search Integration  
✅ Streamlit Interactive UI  
✅ Groq LLM Integration  

---

# 🧠 Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend |
| Streamlit | Frontend UI |
| Groq API | LLM Responses |
| FAISS | Vector Database |
| Sentence Transformers | Text Embeddings |
| SQLite | Student Database |
| Pandas | Excel Handling |
| PyPDF | PDF Parsing |
| SerpAPI | Google Web Search |
| LangChain | GenAI Framework |

---

# 📂 Project Structure

```bash
UniversityAcademicAdvisorBot/
│
├── app.py
├── .env
├── requirements.txt
│
├── data/
│   ├── pdfs/
│   │   ├── DUTY-CHART.pdf
│   │   └── holi_notice.pdf
│   │
│   └── usb_records.xlsx
│
├── utils/
│   ├── llm.py
│   └── embeddings.py
│
├── rag/
│   ├── vector_store.py
│   └── rag_pipeline.py
│
├── sql_agent/
│   ├── database.py
│   └── sql_agent.py
│
├── web_search/
│   └── web_search.py
│
└── router/
    └── smart_router.py