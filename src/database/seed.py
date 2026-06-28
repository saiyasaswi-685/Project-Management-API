import logging

from src.core.security import hash_password
from src.database.database import SessionLocal
from src.database.models import Project, User

logger = logging.getLogger(__name__)


def seed_database():
    db = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter(User.email == "demo@example.com")
            .first()
        )

        if user is None:
            user = User(
                email="demo@example.com",
                hashed_password=hash_password("Password123"),
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            project = Project(
                name="Demo Project",
                description="Initial project created during database seeding.",
                owner_id=user.id,
            )

            db.add(project)
            db.commit()

            logger.info("Demo user and project created successfully.")

        else:
            logger.info("Seed data already exists.")

    except Exception as e:
        logger.error(f"Database seeding failed: {e}")
        db.rollback()
        raise

    finally:
        db.close()