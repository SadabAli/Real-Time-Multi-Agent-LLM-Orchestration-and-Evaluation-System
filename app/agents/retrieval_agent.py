from app.core.llm import llm


def retrieval_agent(query: str):

    chunk_1 = {
        "id": "chunk_1",
        "text": "OpenAI was founded in 2015."
    }

    chunk_2 = {
        "id": "chunk_2",
        "text": "Sam Altman became CEO of OpenAI."
    }

    prompt = f"""
    Use BOTH chunks to answer the query.

    Query:
    {query}

    Chunk 1:
    {chunk_1}

    Chunk 2:
    {chunk_2}

    Cite which chunk contributed to which answer part.
    """

    response = llm.invoke(prompt)

    return {
        "response": response.content,
        "chunks_used": [chunk_1, chunk_2]
    }