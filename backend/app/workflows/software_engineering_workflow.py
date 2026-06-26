from app.registry.register_agents import create_agent_registry
from app.state.workflow_state import WorkflowState


class SoftwareEngineeringWorkflow:

    def __init__(self):
        self.registry = create_agent_registry()

    def run(
        self,
        user_request: str,
        project_path: str,
    ) -> WorkflowState:

        state: WorkflowState = {
            "user_request": user_request,
            "project_path": project_path,
            "current_agent": "",
            "completed_agents": [],
            "artifacts": {},
            "messages": [],
        }

        execution_order = [
            "Engineering Manager",
            "Product Manager",
            "Requirements Analyst",
            "System Architect",
            "Repository Analyst",
            "Scrum Manager"
        ]

        for agent_name in execution_order:

            agent = self.registry.get(agent_name)

            state = agent.execute(state)

        return state