import math
import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.models.task import Task, Tag
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut, PaginatedTasks, TaskStatus, Priority
from app.core.security import get_current_user

router = APIRouter()


def _task_query(owner_id: uuid.UUID):
    return (
        select(Task)
        .where(Task.owner_id == owner_id, Task.archived.is_(False))
        .options(
            selectinload(Task.tags),
            selectinload(Task.project_folder),
            selectinload(Task.sub_tasks),
        )
    )


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(
    payload: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = Task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        priority=payload.priority,
        due_date=payload.due_date,
        folder_id=payload.folder_id,
        parent_id=payload.parent_id,
        owner_id=current_user.id,
    )
    if payload.tag_ids:
        result = await db.execute(
            select(Tag).where(Tag.id.in_(payload.tag_ids), Tag.owner_id == current_user.id)
        )
        task.tags = list(result.scalars().all())

    db.add(task)
    await db.flush()
    await db.refresh(task, ["tags", "project_folder", "sub_tasks"])
    return task


@router.get("", response_model=PaginatedTasks)
async def list_tasks(
    q: Optional[str] = Query(None),
    status: Optional[TaskStatus] = None,
    priority: Optional[Priority] = None,
    folder_id: Optional[uuid.UUID] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = _task_query(current_user.id)

    if q:
        query = query.where(
            or_(Task.title.ilike(f"%{q}%"), Task.description.ilike(f"%{q}%"))
        )
    if status:
        query = query.where(Task.status == status)
    if priority:
        query = query.where(Task.priority == priority)
    if folder_id:
        query = query.where(Task.folder_id == folder_id)

    count_result = await db.execute(
        select(func.count()).select_from(query.subquery())
    )
    total = count_result.scalar_one()

    offset = (page - 1) * page_size
    result = await db.execute(query.offset(offset).limit(page_size))
    items = list(result.scalars().all())

    return PaginatedTasks(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=math.ceil(total / page_size) if total else 0,
    )


@router.get("/{task_id}", response_model=TaskOut)
async def get_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        _task_query(current_user.id).where(Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskOut)
async def update_task(
    task_id: uuid.UUID,
    payload: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        _task_query(current_user.id).where(Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = payload.model_dump(exclude_unset=True, exclude={"tag_ids"})
    for field, value in update_data.items():
        setattr(task, field, value)

    if payload.tag_ids is not None:
        tag_result = await db.execute(
            select(Tag).where(Tag.id.in_(payload.tag_ids), Tag.owner_id == current_user.id)
        )
        task.tags = list(tag_result.scalars().all())

    await db.flush()
    await db.refresh(task, ["tags", "project_folder", "sub_tasks"])
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.owner_id == current_user.id)
    )
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.archived = True
