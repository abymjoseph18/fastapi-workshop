from enum import Enum


class TaskStatusEnum(str, Enum):
    to_do = "To Do"
    in_progress = "In Progress"
    done = "Done"
