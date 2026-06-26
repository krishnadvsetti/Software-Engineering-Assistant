from app.agents.base.base_agent import BaseAgent
from app.artifacts.requirements import RequirementsArtifact
from app.state.workflow_state import WorkflowState


class RequirementsAnalyst(BaseAgent):

    def execute(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        state["current_agent"] = "Requirements Analyst"

        state["completed_agents"].append(
            "Requirements Analyst"
        )

        state["artifacts"]["requirements"] = (
            RequirementsArtifact(
                functional=[
                    "User authentication",
                    "Dashboard",
                    "REST API",
                ],
                non_functional=[
                    "High Availability",
                    "Secure Authentication",
                ],
            ).to_dict()
        )

        state["messages"].append(
            "Requirements Specification created."
        )

        return state