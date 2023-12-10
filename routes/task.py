from enum import Enum
from typing import List

from fastapi import APIRouter, Query, Path, HTTPException
from pydantic import BaseModel

task_router = APIRouter()


class StatusEnum(str, Enum):
    to_do = "To Do"
    in_progress = "In Progress"
    done = "Done"

# Pydantic model for task
class TaskBaseModel(BaseModel):
    task_id: int
    title: str
    description: str
    status: StatusEnum


# Sample task_db dictionary
task_db = {
    1: TaskBaseModel(
        task_id=1,
        title="Complete Feature X",
        description="Implement and test Feature X",
        status=StatusEnum.in_progress,
    ),
    2: TaskBaseModel(
        task_id=2,
        title="Bug Fixing",
        description="Fix bugs reported by QA",
        status=StatusEnum.to_do,
    ),
}


# Example 1: Path Parameter Example
@task_router.get(
    "/tasks/{task_id}",
    summary="Retrieve Task Details",
    description="Get details of a task by providing its ID.",
    response_description="JSON response containing task details.",
    tags=["Tasks"],
    response_model=TaskBaseModel,
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
    response_model=List[TaskBaseModel],
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
    response_model=TaskBaseModel,
)
async def create_new_task(
    title: str = Query(..., title="Task Title"),
    description: str = Query(..., title="Task Description"),
    status: str = Query(..., title="Task Status"),
):
    """Create a new task."""
    # Generating a new task_id
    new_task_id = max(task_db.keys(), default=0) + 1
    new_task = TaskBaseModel(
        task_id=new_task_id, title=title, description=description, status=status
    )
    task_db[new_task_id] = new_task
    return new_task
