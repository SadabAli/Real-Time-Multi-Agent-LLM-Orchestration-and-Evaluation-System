from app.db.database import SessionLocal
from app.db.models import ExecutionTrace


def log_execution(
    job_id,
    agent,
    event_type,
    input_data,
    output_data,
    latency,
    token_count,
    policy_violation=""
):

    db = SessionLocal()

    trace = ExecutionTrace(
        job_id=job_id,
        agent=agent,
        event_type=event_type,
        input_data=str(input_data),
        output_data=str(output_data),
        latency=latency,
        token_count=token_count,
        policy_violation=policy_violation
    )

    db.add(trace)

    db.commit()

    db.close()