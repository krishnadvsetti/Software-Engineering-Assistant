from app.agents.base.base_agent import BaseAgent
from app.state.workflow_state import WorkflowState


class EngineeringManager(BaseAgent):

    def execute(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        state["current_agent"] = "Engineering Manager"

        state["completed_agents"].append(
            "Engineering Manager"
        )

        state["messages"].append(
            "Engineering Manager accepted the request."
        )

        return state