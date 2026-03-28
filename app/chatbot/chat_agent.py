from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def chat_agent(message):

    result = llm.invoke(message)

    return result.content