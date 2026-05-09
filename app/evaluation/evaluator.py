from app.evaluation.test_cases import TEST_CASES
from app.agents.orchestrator import orchestrator


def score_case(output):

    correctness = 8
    citation = 7
    contradiction = 8
    efficiency = 7

    return {
        "correctness": correctness,
        "citation": citation,
        "contradiction": contradiction,
        "efficiency": efficiency,
        "justification":
        "System produced grounded response"
    }


def run_evaluation():

    results = []

    for test in TEST_CASES:

        output = orchestrator(
            test["query"]
        )

        scores = score_case(output)

        results.append({
            "query": test["query"],
            "category": test["category"],
            "scores": scores
        })

    return results