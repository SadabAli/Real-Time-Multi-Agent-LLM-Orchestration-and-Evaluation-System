from typing import TypedDict, Any
# This creates:

# standardized tool outputs
# explicit failure contracts

class ToolResponse(TypedDict):

    status: str

    tool_name: str

    result: Any

    latency: float

    error: str | None