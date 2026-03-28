from langchain_openai import ChatOpenAI
from app.tools.rag_tool import get_rag_tool
from langgraph.prebuilt import create_react_agent

def get_rag_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [get_rag_tool()]
    
    return create_react_agent(llm, tools)

async def rag_node(state):
    agent = get_rag_agent()
    result = await agent.ainvoke({"messages": state["messages"]})
    return {"messages": result["messages"][-1:]}
