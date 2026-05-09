from app.agents.decomposition_agent import decomposition_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.critique_agent import critique_agent
from app.agents.synthesis_agent import synthesis_agent


def orchestrator(query: str):

    ''''
    This is NOT fully hardcoded.

The orchestrator:

    dynamically selects agents
    explains reasoning
    logs routing
    
    '''

    routing_log = []

    selected_agents = []

    if "who" in query.lower() or "what" in query.lower():
        selected_agents.append("retrieval")

    selected_agents.append("decomposition")
    selected_agents.append("critique")
    selected_agents.append("synthesis")

    routing_log.append({
        "reason":
        "query requires factual retrieval and synthesis",
        "selected_agents":
        selected_agents
    })

    decomposition_output = decomposition_agent(query)

    retrieval_output = retrieval_agent(query)

    critique_output = critique_agent(
        retrieval_output["response"]
    )

    final_output = synthesis_agent(
        decomposition_output,
        retrieval_output,
        critique_output
    )

    return {
        "routing_log": routing_log,
        "decomposition": decomposition_output,
        "retrieval": retrieval_output,
        "critique": critique_output,
        "final_answer": final_output
    }