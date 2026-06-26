from pydantic import BaseModel, ConfigDict


class WorkflowRequest(BaseModel):
    user_request: str


class WorkflowResponse(BaseModel):
    user_request: str
    current_agent: str
    completed_agents: list[str]
    artifacts: dict
    messages: list[str]

    model_config = ConfigDict(
        from_attributes=True,
    )