from langchain_openai import OpenAIEmbeddings

def get_embeddings():
    # OpenAIEmbeddings automatically reads OPENAI_API_KEY from environment 
    # (which you load via load_dotenv() in config.py)
    return OpenAIEmbeddings(model="text-embedding-3-small")
