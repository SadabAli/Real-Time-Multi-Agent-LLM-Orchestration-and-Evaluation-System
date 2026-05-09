from app.tools.web_search_tool import web_search_tool


def execute_with_retry(query):

    logs = []

    for attempt in range(3):

        result = web_search_tool(query)

        logs.append({
            "attempt": attempt + 1,
            "result": result
        })

        if result["status"] == "success":

            return {
                "final_result": result,
                "logs": logs
            }

    return {
        "final_result": result,
        "logs": logs
    }