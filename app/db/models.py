from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ExecutionTrace(Base):

    __tablename__ = "execution_traces"

    id = Column(Integer, primary_key=True)

    job_id = Column(String)

    agent = Column(String)

    event_type = Column(String)

    input_data = Column(Text)

    output_data = Column(Text)

    latency = Column(Float)

    token_count = Column(Integer)

    policy_violation = Column(String)


class EvaluationRun(Base):

    __tablename__ = "evaluation_runs"

    id = Column(Integer, primary_key=True)

    test_case = Column(Text)

    category = Column(String)

    correctness_score = Column(Float)

    citation_score = Column(Float)

    contradiction_score = Column(Float)

    efficiency_score = Column(Float)

    justification = Column(Text)


class PromptRewrite(Base):

    __tablename__ = "prompt_rewrites"

    id = Column(Integer, primary_key=True)

    agent_name = Column(String)

    old_prompt = Column(Text)

    new_prompt = Column(Text)

    justification = Column(Text)

    status = Column(String)