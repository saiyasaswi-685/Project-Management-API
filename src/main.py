from contextlib import asynccontextmanager

from fastapi import FastAPI

import src.database.models
from src.api.auth import router as auth_router
from src.api.users import router as users_router
from src.api.projects import router as projects_router
from src.database.database import Base, engine
from src.api.tasks import router as tasks_router

from src.database.seed import seed_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_database()
    yield

app = FastAPI(
    title="Project Management API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(projects_router)
app.include_router(tasks_router)


@app.get("/")
def home():
    return {
        "message": "Project Management API is running"
    }