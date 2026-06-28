from fastapi import APIRouter, Depends

from src.core.security import get_current_user
from src.schemas.user import UserResponse

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_logged_in_user(
    current_user=Depends(get_current_user),
):
    return current_user