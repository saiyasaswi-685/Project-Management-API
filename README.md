# 🚀 Project Management API

A RESTful **Project Management API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**. This backend application enables users to securely register, authenticate, manage projects, and organize tasks through a well-structured REST API.

---

## 📌 Features

### 🔐 Authentication

* User Registration
* User Login
* JWT Bearer Token Authentication
* Get Current Logged-in User

### 📁 Project Management

* Create Project
* Get All Projects
* Get Project by ID
* Update Project
* Delete Project

### ✅ Task Management

* Create Task
* Get All Tasks for a Project
* Get Task by ID
* Update Task
* Delete Task

### 🐳 DevOps
- Docker Support
- Docker Compose Configuration
- Environment Variable Configuration
- PostgreSQL Database

### 🌱 Database
- Automatic Database Seeding
- Demo User and Project Creation

### 🧪 Testing
- Unit Tests (Pytest)
- Integration Tests (Pytest)
- 22 Automated Tests Passed

### 📖 API Documentation
- Interactive Swagger UI
- OpenAPI Documentation
---

## 🛠️ Tech Stack

| Category          | Technologies           |
| ----------------- | ---------------------- |
| Backend           | FastAPI, Python        |
| Database          | PostgreSQL             |
| ORM               | SQLAlchemy             |
| Authentication    | JWT (JSON Web Token)   |
| Validation        | Pydantic               |
| API Documentation | Swagger UI (OpenAPI)   |
| Containerization  | Docker, Docker Compose |
| Testing           | Pytest                 |
| Server            | Uvicorn                |

---

## 📂 Project Structure

```text
project-management-api/
│
├── src/
│   ├── api/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── projects.py
│   │   └── tasks.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── security.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── repository.py
│   │   └── seed.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── project_service.py
│   │   └── task_service.py
│   │
│   └── main.py
│
├── tests/
│   ├── integration/
│   │   └── test_api.py
│   │
│   ├── unit/
│   │   ├── test_auth.py
│   │   ├── test_projects.py
│   │   └── test_tasks.py
│   │
│   └── conftest.py
│
├── screenshots/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/project-management-api.git

cd project-management-api
```

---

### Build and Run Using Docker

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

## ⚙️ Environment Variables

Create a `.env` file using the following template:

```env
DATABASE_URL=postgresql://user:password@db:5432/projectdb

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📖 API Endpoints

### Authentication

| Method | Endpoint             | Description                     |
| ------ | -------------------- | ------------------------------- |
| POST   | `/api/auth/register` | Register a new user             |
| POST   | `/api/auth/login`    | User Login                      |
| POST   | `/api/auth/token`    | Login for Swagger Authorization |
| GET    | `/api/users/me`      | Get Current User                |

---

### Projects

| Method | Endpoint                     | Description       |
| ------ | ---------------------------- | ----------------- |
| POST   | `/api/projects`              | Create Project    |
| GET    | `/api/projects`              | Get All Projects  |
| GET    | `/api/projects/{project_id}` | Get Project by ID |
| PUT    | `/api/projects/{project_id}` | Update Project    |
| DELETE | `/api/projects/{project_id}` | Delete Project    |

---

### Tasks

| Method | Endpoint                           | Description          |
| ------ | ---------------------------------- | -------------------- |
| POST   | `/api/tasks/projects/{project_id}` | Create Task          |
| GET    | `/api/tasks/project/{project_id}`  | Get Tasks by Project |
| GET    | `/api/tasks/{task_id}`             | Get Task by ID       |
| PUT    | `/api/tasks/{task_id}`             | Update Task          |
| DELETE | `/api/tasks/{task_id}`             | Delete Task          |

---

## 🔒 Authentication

This project uses **JWT Bearer Token Authentication**.

Workflow:

1. Register a new user
2. Login to receive a JWT Access Token
3. Click **Authorize** in Swagger UI
4. Authenticate using your credentials
5. Access protected endpoints

---

## 🧪 API Testing

All endpoints have been tested using:

- Swagger UI (Manual API Testing)
- Pytest (Unit Tests)
- Pytest (Integration Tests)

The project includes testing screenshots inside the `screenshots/` directory.

---

## 📸 API Testing Screenshots

```
screenshots/
├── 01-register-success.png
├── 02-login-success.png
├── 03-get-current-user-success.png
├── 04-create-project-success.png
├── 05-get-all-projects-success.png
├── 06-get-project-by-id-success.png
├── 07-update-project-success.png
├── 08-delete-project-success.png
├── 09-create-task-success.png
├── 10-get-all-tasks-success.png
├── 11-get-task-by-id-success.png
├── 12-update-task-success.png
└── 13-delete-task-success.png
```

---

## 📈 Project Status

✅ User Authentication Completed

✅ Project CRUD Operations Completed

✅ Task CRUD Operations Completed

✅ JWT Authentication Implemented

✅ Dockerized Application

✅ Swagger API Documentation

✅ Unit Testing

✅ Integration Testing
---
## 🧪 Testing

This project includes automated tests using **Pytest**.

### Unit Tests
- Authentication Service
- Project Service
- Task Service

### Integration Tests
- API endpoint testing using FastAPI TestClient

Run all tests:

```bash
pytest -v
```

Generate a coverage report:

```bash
pytest --cov=src
```

Current Status:

- ✅ 22 Tests Passed

## 👩‍💻 Author

**Siripurapu Veera Venkata Vishnu Swetha**

Computer Science & Engineering Student

Passionate about Backend Development, Cloud Computing, DevOps, and AI.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
