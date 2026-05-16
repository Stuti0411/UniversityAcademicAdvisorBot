import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)  # Assuming 384-dimensional embeddings
        self.texts = [] 

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype('float32'))
        self.texts.extend(texts)

    def search(self, query_embedding, k=3):
        D, I = self.index.search(np.array([query_embedding]), k)
        return [self.texts[i] for i in I[0]]