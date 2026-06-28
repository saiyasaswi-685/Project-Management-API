from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.core.security import get_current_user
from src.database.database import get_db
from src.database.models import User
from src.database.repository import ProjectRepository
from src.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
)
from src.services.project_service import ProjectService

router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project(
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.create_project(
        name=request.name,
        description=request.description,
        owner_id=current_user.id,
    )


@router.get(
    "",
    response_model=list[ProjectResponse],
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.get_projects(
        owner_id=current_user.id,
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.get_project(
        project_id=project_id,
        owner_id=current_user.id,
    )

@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project(
    project_id: int,
    request: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.update_project(
        project_id=project_id,
        name=request.name,
        description=request.description,
        owner_id=current_user.id,
    )

@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)
    service = ProjectService(repository)

    service.delete_project(
        project_id=project_id,
        owner_id=current_user.id,
    )