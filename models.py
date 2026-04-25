from typing import Optional
from pydantic import BaseModel
from enum import Enum

class TaskStatus(str, Enum):
    todo = "To Do"
    in_progress = "In Progress"
    completed = "Completed"

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo