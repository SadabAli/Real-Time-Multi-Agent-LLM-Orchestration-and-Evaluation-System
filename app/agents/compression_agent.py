from app.core.llm import llm


def compression_agent(text: str):

    prompt = f"""
    Compress this context.

    Preserve:
    - citations
    - JSON
    - tool outputs
    - scores

    Summarize conversational filler only.

    Context:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content