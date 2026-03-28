from typing import TypedDict, Optional

class ProjectState(TypedDict):
    """
    Represents the state of the software generation process shared between all agents.
    """
    user_request: str
    plan: Optional[str]
    backend_code: Optional[str]
    frontend_code: Optional[str]
    qa_feedback: Optional[str]
    is_approved: Optional[bool]
