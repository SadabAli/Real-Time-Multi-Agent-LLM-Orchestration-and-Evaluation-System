import time
# This already satisfies:

# structured results
# relevance scores
# failure contract

def web_search_tool(query: str):

    start = time.time()

    if not query.strip():

        return {
            "status": "malformed_input",
            "tool_name": "web_search",
            "result": None,
            "latency": 0,
            "error": "empty query"
        }

    results = [
        {
            "title": "OpenAI Official",
            "url": "https://openai.com",
            "relevance_score": 0.95
        },
        {
            "title": "Wikipedia OpenAI",
            "url": "https://wikipedia.org",
            "relevance_score": 0.90
        }
    ]

    latency = round(time.time() - start, 2)

    return {
        "status": "success",
        "tool_name": "web_search",
        "result": results,
        "latency": latency,
        "error": None
    }