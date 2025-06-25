from langchain_app.embed_docs import embed_and_store

try:
    print("📦 Starting embedding of knowledge base...")
    embed_and_store()
    print("✅ Embedding completed and FAISS DB saved.")
except Exception as e:
    print(f"❌ ERROR in run_embed.py: {e}")
