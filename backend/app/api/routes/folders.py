import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from pydantic import BaseModel

from app.db.database import get_db
from app.models.task import ProjectFolder, Task
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()


class FolderCreate(BaseModel):
    name: str
    color: str = "#FFE500"


class FolderOut(BaseModel):
    id: uuid.UUID
    name: str
    color: str
    task_count: int = 0
    model_config = {"from_attributes": True}


@router.get("", response_model=list[FolderOut])
async def list_folders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(ProjectFolder).where(ProjectFolder.owner_id == current_user.id)
    )
    folders = list(result.scalars().all())

    out = []
    for folder in folders:
        count_result = await db.execute(
            select(func.count(Task.id)).where(
                Task.folder_id == folder.id, Task.archived.is_(False)
            )
        )
        out.append(FolderOut(
            id=folder.id,
            name=folder.name,
            color=folder.color,
            task_count=count_result.scalar_one(),
        ))
    return out


@router.post("", response_model=FolderOut, status_code=status.HTTP_201_CREATED)
async def create_folder(
    payload: FolderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    folder = ProjectFolder(
        name=payload.name, color=payload.color, owner_id=current_user.id
    )
    db.add(folder)
    await db.flush()
    await db.refresh(folder)
    return FolderOut(id=folder.id, name=folder.name, color=folder.color, task_count=0)


@router.delete("/{folder_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_folder(
    folder_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(ProjectFolder).where(
            ProjectFolder.id == folder_id, ProjectFolder.owner_id == current_user.id
        )
    )
    folder = result.scalar_one_or_none()
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    await db.delete(folder)
