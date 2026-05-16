from rag.rag_pipeline import load_pdfs, ask_rag

load_pdfs()

while True:
    question = input("Ask Question: ")
    answer = ask_rag(question)
    print("\nAnswer:", answer)