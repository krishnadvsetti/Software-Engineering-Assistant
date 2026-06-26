from typing import Any

from typing_extensions import TypedDict


class WorkflowState(TypedDict):

    user_request: str

    project_path: str

    current_agent: str

    completed_agents: list[str]

    artifacts: dict[str, Any]

    messages: list[str]