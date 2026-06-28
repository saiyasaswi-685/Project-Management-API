from src.core.exceptions import (
    forbidden,
    not_found,
)
from src.database.models import Task
from src.database.repository import (
    ProjectRepository,
    TaskRepository,
)


class TaskService:

    def __init__(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def create_task(
        self,
        project_id: int,
        title: str,
        description: str | None,
        status,
        due_date,
        owner_id: int,
    ) -> Task:

        project = self.project_repository.get_project_by_id(project_id)

        if project is None:
            not_found("Project not found")

        if project.owner_id != owner_id:
            forbidden("You are not allowed to access this project")

        return self.task_repository.create_task(
            title=title,
            description=description,
            status=status,
            due_date=due_date,
            project_id=project_id,
        )

    def get_tasks(
        self,
        project_id: int,
        owner_id: int,
    ):

        project = self.project_repository.get_project_by_id(project_id)

        if project is None:
            not_found("Project not found")

        if project.owner_id != owner_id:
            forbidden("You are not allowed to access this project")

        return self.task_repository.get_tasks_by_project(project_id)

    def get_task(
        self,
        task_id: int,
        owner_id: int,
    ) -> Task:

        task = self.task_repository.get_task_by_id(task_id)

        if task is None:
            not_found("Task not found")

        project = self.project_repository.get_project_by_id(task.project_id)

        if project.owner_id != owner_id:
            forbidden("You are not allowed to access this task")

        return task

    def update_task(
        self,
        task_id: int,
        title: str,
        description: str | None,
        status,
        due_date,
        owner_id: int,
    ) -> Task:

        task = self.get_task(
            task_id=task_id,
            owner_id=owner_id,
        )

        return self.task_repository.update_task(
            task=task,
            title=title,
            description=description,
            status=status,
            due_date=due_date,
        )

    def delete_task(
        self,
        task_id: int,
        owner_id: int,
    ):

        task = self.get_task(
            task_id=task_id,
            owner_id=owner_id,
        )

        self.task_repository.delete_task(task)