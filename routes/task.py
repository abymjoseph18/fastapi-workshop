from typing import List

from fastapi import APIRouter, Query, Path, HTTPException, Body

from enums.task_status import TaskStatusEnum
from models.task import TaskResponseBaseModel, TaskUpdateBaseModel, TaskInputBaseModel

task_router = APIRouter()

# Sample task_db dictionary
task_db = {
    1: TaskResponseBaseModel(
        task_id=1,
        title="Complete Feature X",
        description="Implement and test Feature X",
        status=TaskStatusEnum.in_progress,
    ),
    2: TaskResponseBaseModel(
        task_id=2,
        title="Bug Fixing",
        description="Fix bugs reported by QA",
        status=TaskStatusEnum.to_do,
    ),
}


# Example 1: Path Parameter Example
@task_router.get(
    "/tasks/{task_id}",
    summary="Retrieve Task Details",
    description="Get details of a task by providing its ID.",
    response_description="JSON response containing task details.",
    tags=["Tasks"],
    response_model=TaskResponseBaseModel,
)
async def get_task_details(task_id: int = Path(..., title="Task ID", ge=1)):
    """Get details of a task by providing its ID."""
    task = task_db.get(task_id)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")


# Example 2: Query Parameter Example
@task_router.get(
    "/list-tasks",
    summary="List Tasks",
    description="List the details of the first N tasks. If not provided, list all tasks.",
    response_description="JSON response containing list of tasks.",
    tags=["Tasks"],
    response_model=List[TaskResponseBaseModel],
)
async def list_tasks(
    n: int = Query(None, title="Number of Tasks", gt=0, le=len(task_db))
):
    """List the details of the first N tasks. If not provided, list all tasks."""
    if n is not None:
        # Extracting the first N tasks from the task_db dictionary
        first_n_tasks = list(task_db.values())[:n]
        return first_n_tasks
    else:
        # If n is not provided, list all tasks
        return list(task_db.values())


# Example 3: Create New Task
@task_router.post(
    "/create-task",
    summary="Create New Task",
    description="Create a new task.",
    response_description="JSON response confirming the creation of the task.",
    tags=["Tasks"],
    response_model=TaskResponseBaseModel,
)
async def create_new_task(task_data: TaskInputBaseModel):
    """Create a new task."""
    # Generating a new task_id
    new_task_id = max(task_db.keys(), default=0) + 1
    new_task = task_data.copy(update={"task_id": new_task_id})
    task_db[new_task_id] = new_task
    return new_task


# Example 4: Update Task
@task_router.put(
    "/update-task/{task_id}",
    summary="Update Task",
    description="Update the details of an existing task by providing its ID.",
    response_description="JSON response confirming the update of the task.",
    tags=["Tasks"],
    response_model=TaskResponseBaseModel,
)
async def update_task(
    task_id: int = Path(..., title="Task ID", ge=1),
    update_data: TaskUpdateBaseModel = Body(..., title="Update Data"),
):
    """Update the details of an existing task by providing its ID."""
    task = task_db.get(task_id)
    if task:
        # Update the task details
        for field, value in update_data.dict().items():
            if value is not None:
                setattr(task, field, value)
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")


# Example 5: Delete Task
@task_router.delete(
    "/delete-task/{task_id}",
    summary="Delete Task",
    description="Delete an existing task by providing its ID.",
    response_description="JSON response confirming the deletion of the task.",
    tags=["Tasks"],
    response_model=TaskResponseBaseModel,
)
async def delete_task(task_id: int = Path(..., title="Task ID", ge=1)):
    """Delete an existing task by providing its ID."""
    task = task_db.pop(task_id, None)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")
