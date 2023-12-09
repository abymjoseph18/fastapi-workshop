from fastapi import APIRouter, Query, Path, HTTPException

task_router = APIRouter()

# Sample task_db dictionary
task_db = {
    1: {"task_id": 1, "title": "Complete Feature X", "description": "Implement and test Feature X",
        "status": "In Progress"},
    2: {"task_id": 2, "title": "Bug Fixing", "description": "Fix bugs reported by QA", "status": "To Do"},
}


# Example 1: Path Parameter Example
@task_router.get(
    "/tasks/{task_id}",
    summary="Retrieve Task Details",
    description="Get details of a task by providing its ID.",
    response_description="JSON response containing task details.",
    tags=["Tasks"],
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
    description="List the details of the first N tasks. If N is not provided, list all tasks.",
    response_description="JSON response containing list of tasks.",
    tags=["Tasks"],
)
async def list_tasks(n: int = Query(None, title="Number of Tasks", gt=0, le=len(task_db))):
    """List the details of the first N tasks. If N is not provided, list all tasks."""
    # Extracting the first N tasks from the task_db dictionary
    if n is not None:
        first_n_tasks = list(task_db.values())[:n]
        return first_n_tasks
    else:
        return list(task_db.values())
