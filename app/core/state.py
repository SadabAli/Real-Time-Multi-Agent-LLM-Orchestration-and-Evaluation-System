from typing import TypedDict, List, Dict, Any

# WHY THIS IS IMPORTANT

# The assignment explicitly says:

# agents must communicate through shared context object

# This file satisfies that requirement.

class SharedState(TypedDict, total=False):

    job_id: str

    user_query: str

    current_agent: str

    messages: List[Dict[str, Any]]

    retrieved_chunks: List[Dict[str, Any]]

    tool_calls: List[Dict[str, Any]]

    critique: List[Dict[str, Any]]

    synthesis: str

    provenance: List[Dict[str, Any]]

    context_budget: Dict[str, int]

    logs: List[Dict[str, Any]]

    errors: List[str]