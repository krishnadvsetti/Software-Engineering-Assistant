from abc import ABC, abstractmethod

from app.state.workflow_state import WorkflowState


class BaseAgent(ABC):

    @abstractmethod
    def execute(
        self,
        state: WorkflowState,
    ) -> WorkflowState:
        pass