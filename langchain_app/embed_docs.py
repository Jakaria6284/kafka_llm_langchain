from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
import sys

def embed_and_store():
    try:
        csv_path = "data/sample_qa_100.csv"
        print(f"📦 Starting embedding of knowledge base...")
        
        # Debug: Print absolute path
        print(f"Checking if file exists at: {os.path.abspath(csv_path)}")
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at {os.path.abspath(csv_path)}")
        
        print(f"📄 Loading documents from CSV: {csv_path}")
        loader = CSVLoader(file_path=csv_path, source_column="answer")  # Changed to "answer"
        documents = loader.load()
        print(f"✅ Loaded {len(documents)} documents")
        
        print("🔢 Generating embeddings...")
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.from_documents(documents, embedding)
        
        print("💾 Saving FAISS index...")
        db.save_local("faiss_index")
        print("✅ FAISS index created and stored.")
    
    except Exception as e:
        print(f"❌ ERROR in embed_docs.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
    embed_and_store()