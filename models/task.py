from pydantic import BaseModel, Field

from enums.task_status import TaskStatusEnum


# Pydantic model for task
class TaskResponseBaseModel(BaseModel):
    task_id: int = Field(None, title="Task ID")
    title: str = Field(..., title="Task Title", min_length=1, max_length=100)
    description: str = Field(
        ..., title="Task Description", min_length=1, max_length=500
    )
    status: TaskStatusEnum = Field(..., title="Task Status")


# Pydantic model for creating task
class TaskInputBaseModel(BaseModel):
    title: str = Field(..., title="Task Title", min_length=1, max_length=100)
    description: str = Field(
        ..., title="Task Description", min_length=1, max_length=500
    )
    status: TaskStatusEnum = Field(..., title="Task Status")


# Pydantic model for updating task
class TaskUpdateBaseModel(BaseModel):
    title: str = Field(None, title="Task Title", min_length=1, max_length=100)
    description: str = Field(
        None, title="Task Description", min_length=1, max_length=500
    )
    status: TaskStatusEnum = Field(None, title="Task Status")
