from app.agents.base.base_agent import BaseAgent
from app.state.workflow_state import WorkflowState


class ScrumManager(BaseAgent):

    def execute(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        state["current_agent"] = "Scrum Manager"

        state["completed_agents"].append(
            "Scrum Manager"
        )

        state["artifacts"]["sprint"] = {
            "name": "Sprint 1",
            "status": "Planned",
        }

        state["messages"].append(
            "Sprint planning completed."
        )

        return state