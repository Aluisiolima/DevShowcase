from http import HTTPStatus

from fastapi import APIRouter
from devshowcase.profile.service import ProfileService
from devshowcase.profile.schema import (
    ProfileCreateSchema,
    ProfileUpdateSchema,
    ProfileResponseSchema,
)
from devshowcase.core.types import AsyncSessionDep

profile_router = APIRouter(prefix="/profile", tags=["Profile"])


@profile_router.get(
    "/{id}", response_model=ProfileResponseSchema, status_code=HTTPStatus.CREATED
)
async def get_profile(id: int, session: AsyncSessionDep) -> ProfileResponseSchema:
    return await ProfileService.get_profile_by_id(profile_id=id, db=session)


@profile_router.post(
    "/", response_model=ProfileResponseSchema, status_code=HTTPStatus.CREATED
)
async def create_profile(
    profile: ProfileCreateSchema, session: AsyncSessionDep
) -> ProfileCreateSchema:
    return await ProfileService.create_profile(profile_data=profile, db=session)
