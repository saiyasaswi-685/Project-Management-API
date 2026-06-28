from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from src.services.project_service import ProjectService


class TestProjectService:

    def test_create_project(self):
        repository = MagicMock()

        repository.create_project.return_value = {
            "name": "Test Project"
        }

        service = ProjectService(repository)

        result = service.create_project(
            name="Test Project",
            description="Test Description",
            owner_id=1,
        )

        assert result["name"] == "Test Project"

    def test_get_projects(self):
        repository = MagicMock()

        repository.get_projects_by_owner.return_value = [
            {"name": "Project 1"},
            {"name": "Project 2"},
        ]

        service = ProjectService(repository)

        result = service.get_projects(owner_id=1)

        assert len(result) == 2

    def test_get_project_success(self):
        repository = MagicMock()

        project = MagicMock()
        project.owner_id = 1

        repository.get_project_by_id.return_value = project

        service = ProjectService(repository)

        result = service.get_project(
            project_id=1,
            owner_id=1,
        )

        assert result == project

    def test_get_project_not_found(self):
        repository = MagicMock()

        repository.get_project_by_id.return_value = None

        service = ProjectService(repository)

        with pytest.raises(HTTPException):
            service.get_project(
                project_id=1,
                owner_id=1,
            )

    def test_get_project_forbidden(self):
        repository = MagicMock()

        project = MagicMock()
        project.owner_id = 2

        repository.get_project_by_id.return_value = project

        service = ProjectService(repository)

        with pytest.raises(HTTPException):
            service.get_project(
                project_id=1,
                owner_id=1,
            )

    def test_update_project(self):
        repository = MagicMock()

        project = MagicMock()
        project.owner_id = 1

        repository.get_project_by_id.return_value = project
        repository.update_project.return_value = project

        service = ProjectService(repository)

        result = service.update_project(
            project_id=1,
            name="Updated Project",
            description="Updated Description",
            owner_id=1,
        )

        assert result == project

    def test_delete_project(self):
        repository = MagicMock()

        project = MagicMock()
        project.owner_id = 1

        repository.get_project_by_id.return_value = project

        service = ProjectService(repository)

        service.delete_project(
            project_id=1,
            owner_id=1,
        )

        repository.delete_project.assert_called_once_with(project)