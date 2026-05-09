from app.core.llm import llm


def synthesis_agent(
    decomposition,
    retrieval,
    critique
):

    prompt = f"""
    Merge all outputs.

    Resolve contradictions.

    Generate:
    - final answer
    - provenance map

    Decomposition:
    {decomposition}

    Retrieval:
    {retrieval}

    Critique:
    {critique}
    """

    response = llm.invoke(prompt)

    return response.content