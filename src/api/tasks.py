from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.core.security import get_current_user
from src.database.database import get_db
from src.database.models import User
from src.database.repository import (
    ProjectRepository,
    TaskRepository,
)
from src.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
)
from src.services.task_service import TaskService

router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


@router.post(
    "/projects/{project_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    project_id: int,
    request: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(
        TaskRepository(db),
        ProjectRepository(db),
    )

    return service.create_task(
        project_id=project_id,
        title=request.title,
        description=request.description,
        status=request.status,
        due_date=request.due_date,
        owner_id=current_user.id,
    )


@router.get(
    "/project/{project_id}",
    response_model=list[TaskResponse],
)
def get_tasks(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(
        TaskRepository(db),
        ProjectRepository(db),
    )

    return service.get_tasks(
        project_id=project_id,
        owner_id=current_user.id,
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(
        TaskRepository(db),
        ProjectRepository(db),
    )

    return service.get_task(
        task_id=task_id,
        owner_id=current_user.id,
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    request: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(
        TaskRepository(db),
        ProjectRepository(db),
    )

    return service.update_task(
        task_id=task_id,
        title=request.title,
        description=request.description,
        status=request.status,
        due_date=request.due_date,
        owner_id=current_user.id,
    )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = TaskService(
        TaskRepository(db),
        ProjectRepository(db),
    )

    service.delete_task(
        task_id=task_id,
        owner_id=current_user.id,
    )