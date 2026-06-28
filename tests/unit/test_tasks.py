from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from src.services.task_service import TaskService


class TestTaskService:

    def setup_method(self):
        self.task_repository = MagicMock()
        self.project_repository = MagicMock()

        self.service = TaskService(
            task_repository=self.task_repository,
            project_repository=self.project_repository,
        )

    def test_create_task(self):
        project = MagicMock()
        project.owner_id = 1

        self.project_repository.get_project_by_id.return_value = project

        task = MagicMock()

        self.task_repository.create_task.return_value = task

        result = self.service.create_task(
            project_id=1,
            title="Task 1",
            description="Task Description",
            status="TODO",
            due_date=None,
            owner_id=1,
        )

        assert result == task

    def test_create_task_project_not_found(self):
        self.project_repository.get_project_by_id.return_value = None

        with pytest.raises(HTTPException):
            self.service.create_task(
                project_id=1,
                title="Task",
                description="Desc",
                status="TODO",
                due_date=None,
                owner_id=1,
            )

    def test_get_tasks(self):
        project = MagicMock()
        project.owner_id = 1

        self.project_repository.get_project_by_id.return_value = project

        self.task_repository.get_tasks_by_project.return_value = [
            MagicMock(),
            MagicMock(),
        ]

        result = self.service.get_tasks(
            project_id=1,
            owner_id=1,
        )

        assert len(result) == 2

    def test_get_task(self):
        task = MagicMock()
        task.project_id = 1

        project = MagicMock()
        project.owner_id = 1

        self.task_repository.get_task_by_id.return_value = task
        self.project_repository.get_project_by_id.return_value = project

        result = self.service.get_task(
            task_id=1,
            owner_id=1,
        )

        assert result == task

    def test_get_task_not_found(self):
        self.task_repository.get_task_by_id.return_value = None

        with pytest.raises(HTTPException):
            self.service.get_task(
                task_id=1,
                owner_id=1,
            )

    def test_update_task(self):
        task = MagicMock()
        task.project_id = 1

        project = MagicMock()
        project.owner_id = 1

        self.task_repository.get_task_by_id.return_value = task
        self.project_repository.get_project_by_id.return_value = project
        self.task_repository.update_task.return_value = task

        result = self.service.update_task(
            task_id=1,
            title="Updated Task",
            description="Updated Description",
            status="DONE",
            due_date=None,
            owner_id=1,
        )

        assert result == task

    def test_delete_task(self):
        task = MagicMock()
        task.project_id = 1

        project = MagicMock()
        project.owner_id = 1

        self.task_repository.get_task_by_id.return_value = task
        self.project_repository.get_project_by_id.return_value = project

        self.service.delete_task(
            task_id=1,
            owner_id=1,
        )

        self.task_repository.delete_task.assert_called_once_with(task)