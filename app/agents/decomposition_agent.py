from app.core.llm import llm


def decomposition_agent(query: str):

    prompt = f"""
    Break this query into structured sub-tasks.

    Include:
    - task_id
    - task_description
    - dependencies

    Query:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content