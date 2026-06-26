from app.agents.management.engineering_manager import EngineeringManager
from app.agents.management.product_manager import ProductManager
from app.agents.management.scrum_manager import ScrumManager
from app.registry.agent_registry import AgentRegistry
from app.agents.development.requirements_analyst import RequirementsAnalyst
from app.agents.development.system_architect import SystemArchitect
from app.agents.development.repository_analyst import RepositoryAnalyst


def create_agent_registry() -> AgentRegistry:

    registry = AgentRegistry()

    registry.register(
        "Engineering Manager",
        EngineeringManager(),
    )

    registry.register(
        "Product Manager",
        ProductManager(),
    )

    registry.register(
    "Repository Analyst",
    RepositoryAnalyst(),
    )

    registry.register(
    "System Architect",
    SystemArchitect(),
    )

    registry.register(
    "Requirements Analyst",
    RequirementsAnalyst(),
    )

    registry.register(
        "Scrum Manager",
        ScrumManager(),
    )

    return registry