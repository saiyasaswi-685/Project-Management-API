from src.core.exceptions import (
    forbidden,
    not_found,
)
from src.database.models import Project
from src.database.repository import ProjectRepository

class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def create_project(
        self,
        name: str,
        description: str | None,
        owner_id: int,
    ) -> Project:

        return self.repository.create_project(
            name=name,
            description=description,
            owner_id=owner_id,
        )
    def get_projects(
    self,
    owner_id: int,
    ):
        return self.repository.get_projects_by_owner(owner_id)
    
    def get_project(
        self,
        project_id: int,
        owner_id: int,
    ) -> Project:

        project = self.repository.get_project_by_id(project_id)

        if project is None:
            not_found("Project not found")

        if project.owner_id != owner_id:
            forbidden("You are not allowed to access this project")

        return project
    
    
    def update_project(
    self,
    project_id: int,
    name: str,
    description: str | None,
    owner_id: int,
) -> Project:

        project = self.get_project(
        project_id=project_id,
        owner_id=owner_id,
    )

        return self.repository.update_project(
        project=project,
        name=name,
        description=description,
    )


    def delete_project(
    self,
    project_id: int,
    owner_id: int,
):
        project = self.get_project(
        project_id=project_id,
        owner_id=owner_id,
    )

        self.repository.delete_project(project)