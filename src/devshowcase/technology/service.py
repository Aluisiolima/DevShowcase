from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from devshowcase.core.exceptions import exceptions
from devshowcase.core.repository import Technology
from devshowcase.technology.schema import (
    TechnologyCreateSchema,
    TechnologyResponseSchema,
)
from devshowcase.project.schema import ProjectResponseSchema


class TechnologyService:
    """
    Service class for Technology operations
    """

    @staticmethod
    @exceptions
    async def create_technology(
        technology_data: TechnologyCreateSchema, db: AsyncSession
    ) -> TechnologyResponseSchema:
        """
        Create a new technology entry in the database.

        Args:
            technology_data (TechnologyCreateSchema): The data for the new technology.
            db (AsyncSession): The database session.

        Returns:
            TechnologyResponseSchema: The created technology entry.
        """
        new_technology = Technology(**technology_data.model_dump())
        db.add(new_technology)
        await db.commit()
        await db.refresh(new_technology)
        return TechnologyResponseSchema.model_validate(new_technology)

    @staticmethod
    @exceptions
    async def get_technologys(db: AsyncSession) -> list[TechnologyResponseSchema]:
        """
        Retrieve all technology entries from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            list[TechnologyResponseSchema]: A list of all technology entries.
        """
        result = await db.execute(select(Technology))
        technologies = result.scalars().all()
        return [TechnologyResponseSchema.model_validate(tech) for tech in technologies]
