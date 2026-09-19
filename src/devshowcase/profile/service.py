from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from devshowcase.core.exceptions import exceptions
from devshowcase.core.repository import Profile
from devshowcase.profile.schema import ProfileCreateSchema, ProfileResponseSchema


class ProfileService:
    """
    Service class for Profile operations
    """

    @staticmethod
    @exceptions
    async def create_profile(
        profile_data: ProfileCreateSchema, db: AsyncSession
    ) -> ProfileCreateSchema:
        """
        Create a new profile entry in the database.

        Args:
            profile_data (ProfileCreateSchema): The data for the new profile.
            db (AsyncSession): The database session.

        Returns:
            ProfileCreateSchema: The created profile entry.
        """
        new_profile = Profile(**profile_data.model_dump())
        db.add(new_profile)
        await db.commit()
        await db.refresh(new_profile)
        return ProfileCreateSchema.model_validate(new_profile)

    @staticmethod
    @exceptions
    async def get_profile_by_id(
        profile_id: int, db: AsyncSession
    ) -> ProfileResponseSchema:
        """
        Retrieve a profile entry by its ID.

        Args:
            profile_id (int): The ID of the profile to retrieve.
            db (AsyncSession): The database session.

        Returns:
            ProfileResponseSchema: The retrieved profile entry.

        Raises:
            HTTPException: If the profile with the given ID does not exist.
        """
        result = await db.execute(
            select(Profile)
            .options(selectinload(Profile.projects))
            .where(Profile.id == profile_id)
        )
        profile = result.scalar_one_or_none()
        if not profile:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"Profile with ID {profile_id} not found",
            )
        return ProfileCreateSchema.model_validate(profile)
