import os
from utils.embeddings import get_embedding
from utils.llm import get_llm_response
from rag.vector_store import VectorStore
from pypdf import PdfReader

vector_db = VectorStore()

def load_pdfs():
    pdf_folder = "data/pdfs"
    all_texts = [] 
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file)
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
                chunks = split_text(text)
                all_texts.extend(chunks)
    embeddings = [get_embedding(chunk) for chunk in all_texts]
    vector_db.add(embeddings, all_texts)
    print("PDFs Loaded Successfully")

#Split text into chunks
def split_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

#Ask question
def ask_rag(question):
    query_embedding = get_embedding(question)
    relevant_chunks = vector_db.search(query_embedding)
    context = "\n".join(relevant_chunks)
    prompt = f"Answer the following question based on the provided context:\n\nContext: {context}\n\nQuestion: {question}\nAnswer:"
    response = get_llm_response(prompt)
    return response
