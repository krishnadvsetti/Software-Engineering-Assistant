from app.registry.register_agents import create_agent_registry
from app.state.workflow_state import WorkflowState


class SoftwareEngineeringWorkflow:

    def __init__(self):
        self.registry = create_agent_registry()

    def run(
        self,
        user_request: str,
    ) -> WorkflowState:

        state: WorkflowState = {
            "user_request": user_request,
            "current_agent": "",
            "completed_agents": [],
            "artifacts": {},
            "messages": [],
        }

        execution_order = [
            "Engineering Manager",
            "Product Manager",
            "Requirements Analyst",
            "Scrum Manager",
        ]

        for agent_name in execution_order:

            agent = self.registry.get(agent_name)

            state = agent.execute(state)

        return state