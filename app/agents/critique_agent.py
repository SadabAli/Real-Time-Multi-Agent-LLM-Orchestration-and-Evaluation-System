from app.core.llm import llm


def critique_agent(text: str):

    prompt = f"""
    Review this output carefully.

    Return:
    - claims
    - confidence score
    - disagreements
    - factual concerns

    Text:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content