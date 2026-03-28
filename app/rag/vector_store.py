import os
from langchain_community.vectorstores import Chroma
from app.rag.embeddings import get_embeddings
from app.rag.document_loader import load_and_split_documents

# Store the vector database data locally inside the "rag/chroma_db" folder
CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")

def get_vector_store():
    """Returns the initialized Chroma vector store for querying."""
    return Chroma(
        collection_name="project_knowledge",
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_DB_DIR
    )

def ingest_documents():
    """Utility function to load docs, convert them to vectors, and save them."""
    print("Loading and splitting documents from /documents folder...")
    splits = load_and_split_documents()
    
    if not splits:
        print("No documents found in /documents to ingest.")
        return
        
    print(f"Found {len(splits)} chunks. Ingesting into Vector DB...")
    
    # Convert splits to vectors and persist (save) to disk
    vector_store = Chroma.from_documents(
        documents=splits,
        embedding=get_embeddings(),
        collection_name="project_knowledge",
        persist_directory=CHROMA_DB_DIR
    )
    
    print("Ingestion complete. The database is ready for RAG.")
    return vector_store

# If you run this file directly (python -m app.rag.vector_store), it will populate the DB.
if __name__ == "__main__":
    ingest_documents()
