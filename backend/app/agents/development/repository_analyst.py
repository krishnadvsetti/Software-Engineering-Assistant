from app.agents.base.base_agent import BaseAgent
from app.artifacts.repository_analysis import RepositoryAnalysisArtifact
from app.state.workflow_state import WorkflowState


class RepositoryAnalyst(BaseAgent):

    def execute(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        state["current_agent"] = "Repository Analyst"

        state["completed_agents"].append(
            "Repository Analyst"
        )

        state["artifacts"]["repository_analysis"] = (
            RepositoryAnalysisArtifact(
                language="Python",
                framework="FastAPI",
                database="PostgreSQL",
                package_manager="pip",
                containers=True,
                ci_cd="GitHub Actions",
            ).to_dict()
        )

        state["messages"].append(
            "Repository analyzed."
        )

        return state