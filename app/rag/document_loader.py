import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# We look for a "documents" folder inside the current "rag" directory
DOCS_DIR = os.path.join(os.path.dirname(__file__), "documents")

def load_and_split_documents():
    # Check if directory exists
    if not os.path.exists(DOCS_DIR):
        print(f"Directory {DOCS_DIR} not found. Creating it...")
        os.makedirs(DOCS_DIR)
        return []

    # 1. Load all markdown formatting files in the documents folder
    loader = DirectoryLoader(DOCS_DIR, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    if not documents:
        return []

    # 2. Split text into chunks for better vector retrieval
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(documents)
    
    return splits
