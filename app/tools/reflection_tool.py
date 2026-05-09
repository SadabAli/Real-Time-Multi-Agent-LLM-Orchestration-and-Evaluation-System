def reflection_tool(history):

    if not history:

        return {
            "status": "empty_results",
            "tool_name": "reflection_tool",
            "result": None,
            "latency": 0,
            "error": "no history"
        }

    contradictions = []

    for item in history:

        if "not" in item.lower():

            contradictions.append(item)

    return {
        "status": "success",
        "tool_name": "reflection_tool",
        "result": contradictions,
        "latency": 0.01,
        "error": None
    }