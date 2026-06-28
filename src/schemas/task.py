from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from src.database.models import TaskStatus


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: TaskStatus = TaskStatus.TODO
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: TaskStatus
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    due_date: Optional[datetime]
    project_id: int
    created_at: datetime