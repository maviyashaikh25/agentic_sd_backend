from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = PromptTemplate.from_template("""
Classify the user input into exactly one of these intents:
ACTION (Create, build, or modify a project/feature)
RAG (Ask a question about the project, architecture, or tech)
DEBUG (Fix an error, bug, or failing test)

User Input: {input}

Return ONLY the intent string.
""")

def classify_intent(message: str) -> str:
    chain = prompt | llm
    return chain.invoke({"input": message}).content.strip().upper()
