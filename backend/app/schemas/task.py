import uuid
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    blocked = "blocked"
    done = "done"


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class TagOut(BaseModel):
    id: uuid.UUID
    name: str
    color: str
    model_config = {"from_attributes": True}


class FolderOut(BaseModel):
    id: uuid.UUID
    name: str
    color: str
    model_config = {"from_attributes": True}


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    priority: Priority = Priority.medium
    due_date: Optional[datetime] = None
    folder_id: Optional[uuid.UUID] = None
    parent_id: Optional[uuid.UUID] = None


class TaskCreate(TaskBase):
    tag_ids: Optional[List[uuid.UUID]] = []


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[Priority] = None
    due_date: Optional[datetime] = None
    folder_id: Optional[uuid.UUID] = None
    tag_ids: Optional[List[uuid.UUID]] = None
    archived: Optional[bool] = None


class TaskOut(TaskBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    archived: bool
    tags: List[TagOut] = []
    project_folder: Optional[FolderOut] = None
    sub_tasks: List["TaskOut"] = []
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


TaskOut.model_rebuild()


class PaginatedTasks(BaseModel):
    items: List[TaskOut]
    total: int
    page: int
    page_size: int
    pages: int
