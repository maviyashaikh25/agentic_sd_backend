from langchain_openai import ChatOpenAI
from app.tools.rag_tool import get_rag_tool
from langgraph.prebuilt import create_react_agent

def get_debug_agent():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    tools = [get_rag_tool()] # Debug agent also gets the tool!
    
    # Debug agent thinks: "Error in intent_classifier. Let me retrieve it."
    return create_react_agent(llm, tools)

async def debug_node(state):
    agent = get_debug_agent()
    result = await agent.ainvoke({"messages": state["messages"]})
    return {"messages": result["messages"][-1:]}
