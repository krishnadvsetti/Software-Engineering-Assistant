from fastapi import APIRouter

from app.workflows.software_engineering_workflow import (
    SoftwareEngineeringWorkflow,
)

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"],
)


@router.post("/run")
def run_workflow(request: dict):

    workflow = SoftwareEngineeringWorkflow()

    return workflow.run(
        request["user_request"]
    )