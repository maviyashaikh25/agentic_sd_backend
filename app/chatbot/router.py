from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from app.graph.workflow import graph

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    
    # We initialize the state with the user's message wrapped correctly
    initial_state = {
        "messages": [HumanMessage(content=request.message)]
    }

    # Run the graph asynchronously
    result = await graph.ainvoke(initial_state)
    
    # Extract the final AI message from the updated state
    final_message = result["messages"][-1].content
    
    # Extract the detected intent (helpful for the frontend UI or debugging)
    intent = result.get("intent", "UNKNOWN")

    return {
        "reply": final_message,
        "intent_detected": intent
    }
