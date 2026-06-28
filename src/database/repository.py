from sqlalchemy.orm import Session

from src.database.models import User, Project, Task


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(
        self,
        email: str,
        hashed_password: str,
    ):
        user = User(
            email=email,
            hashed_password=hashed_password,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get_user_by_email(
        self,
        email: str,
    ):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_user_by_id(
        self,
        user_id: int,
    ):
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )


class ProjectRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_project(
        self,
        name: str,
        description: str,
        owner_id: int,
    ):
        project = Project(
            name=name,
            description=description,
            owner_id=owner_id,
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def get_projects_by_owner(
        self,
        owner_id: int,
    ):
        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def get_project_by_id(
        self,
        project_id: int,
    ):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def delete_project(
        self,
        project: Project,
    ):
        self.db.delete(project)
        self.db.commit()

    def update_project(
    self,
    project: Project,
    name: str,
    description: str | None,
):
        project.name = name
        project.description = description

        self.db.commit()
        self.db.refresh(project)

        return project

class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_task(
        self,
        title: str,
        description: str,
        status: str,
        due_date,
        project_id: int,
    ):
        task = Task(
            title=title,
            description=description,
            status=status,
            due_date=due_date,
            project_id=project_id,
        )

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def get_task_by_id(
        self,
        task_id: int,
    ):
        return (
            self.db.query(Task)
            .filter(Task.id == task_id)
            .first()
        )
    
    def update_task(
    self,
    task: Task,
    title: str,
    description: str | None,
    status: str,
    due_date,
):
        task.title = title
        task.description = description
        task.status = status
        task.due_date = due_date

        self.db.commit()
        self.db.refresh(task)

        return task

    def get_tasks_by_project(
        self,
        project_id: int,
    ):
        return (
            self.db.query(Task)
            .filter(Task.project_id == project_id)
            .all()
        )

    def delete_task(
        self,
        task: Task,
    ):
        self.db.delete(task)
        self.db.commit()