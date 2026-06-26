from fastapi import APIRouter

from app.schemas.workflow import (
    WorkflowRequest,
    WorkflowResponse,
)
from app.workflows.software_engineering_workflow import (
    SoftwareEngineeringWorkflow,
)

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"],
)


@router.post(
    "/run",
    response_model=WorkflowResponse,
)
def run_workflow(
    request: WorkflowRequest,
):

    workflow = SoftwareEngineeringWorkflow()

    result = workflow.run(
        request.user_request
    )

    return result