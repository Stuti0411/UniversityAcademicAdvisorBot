from rag.rag_pipeline import ask_rag
from sql_agent.sql_agent import ask_sql
from web_search.web_search import search_web

def route_question(question):
    question_lower = question.lower()

    sql_keywords = ["cgpa", "marks", "attendance", "students", "semester", "department", "score", "points", "result", "average"]
    rag_keywords = ["holiday", "holi", "celebration", "events", "policy", "rule", "notice", "advice", "duty"]
    
    #SQL Questions
    if any(word in question_lower for word in sql_keywords):
        print("Routing to SQL Agent...")
        return ask_sql(question)
    
    #PDF/RAG Questions
    elif any(word in question_lower for word in rag_keywords):
        print("Routing to RAG Agent...")
        return ask_rag(question)
    else:
        return search_web(question)  # Fallback to web search if no keywords match
