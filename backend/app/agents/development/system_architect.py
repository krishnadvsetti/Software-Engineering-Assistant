from app.agents.base.base_agent import BaseAgent
from app.artifacts.architecture import ArchitectureArtifact
from app.state.workflow_state import WorkflowState


class SystemArchitect(BaseAgent):

    def execute(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        state["current_agent"] = "System Architect"

        state["completed_agents"].append(
            "System Architect"
        )

        state["artifacts"]["architecture"] = (
            ArchitectureArtifact(
                architecture_style="Layered Architecture",
                backend="FastAPI",
                frontend="Next.js",
                database="PostgreSQL",
                cache="Redis",
                deployment="Docker",
            ).to_dict()
        )

        state["messages"].append(
            "System architecture designed."
        )

        return state