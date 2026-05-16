import os
from dotenv import load_dotenv
import requests
from utils.llm import get_llm_response

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

def search_web(question):
    params = {
        "engine": "google",
        "q": question,
        "api_key": SERPAPI_KEY,
        "num": 5
    }

    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    snippets =[]
    if "organic_results" in results:
        for item in results["organic_results"]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            snippets.append(f"{title}: {snippet}")
            
    web_context = "\n".join(snippets)
    prompt  = f""" Answer the question using web search results.
    Question : {question}
    Web Search Results: {web_context}
    """
    return get_llm_response(prompt)
