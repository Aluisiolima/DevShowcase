from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from devshowcase.core.exceptions import exceptions
from devshowcase.core.repository import Project
from devshowcase.project.schema import (
    ProjectCreateSchema,
    ProjectResponseSchema,
)
from devshowcase.core.repository import Feedback
from devshowcase.feedback.schema import FeedbackCreateSchema


class ProjectService:
    """
    Service class for Project operations
    """

    @staticmethod
    @exceptions
    async def create_project(
        project_data: ProjectCreateSchema, db: AsyncSession
    ) -> ProjectCreateSchema:
        """
        Create a new project entry in the database.

        Args:
            project_data (ProjectCreateSchema): The data for the new project.
            db (AsyncSession): The database session.

        Returns:
            ProjectCreateSchema: The created project entry.
        """
        new_project = Project(**project_data.model_dump())
        db.add(new_project)
        await db.commit()
        await db.refresh(new_project)
        return ProjectCreateSchema.model_validate(new_project)

    @staticmethod
    @exceptions
    async def get_project_by_id(id: int, db: AsyncSession) -> ProjectResponseSchema:
        """
        Retrieve a project entry by its ID.

        Args:
            profile_id (int): The ID of the profile for which to retrieve projects.
            db (AsyncSession): The database session.

        Returns:
            ProjectResponseSchema: The retrieved project entry.

        Raises:
            HTTPException: If the project with the given ID does not exist.
        """
        result = await db.execute(
            select(Project)
            .options(selectinload(Project.feedbacks))
            .where(Project.id == id)
        )
        project = result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"Project with ID {id} not found.",
            )
        return ProjectResponseSchema.model_validate(project)

    @staticmethod
    @exceptions
    async def add_curtida_project(
        project_id: int, db: AsyncSession
    ) -> ProjectResponseSchema:
        """
        Add a like to a project entry.

        Args:
            project_id (int): The ID of the project to add a like to.
            db (AsyncSession): The database session.

        Returns:
            ProjectResponseSchema: The updated project entry with the new like count.

        Raises:
            HTTPException: If the project with the given ID does not exist.
        """
        result = await db.execute(
            select(Project)
            .options(selectinload(Project.feedbacks))
            .where(Project.id == project_id)
        )
        project = result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"Project with ID {project_id} not found.",
            )

        # Increment the like count
        project.curtidas += 1
        await db.commit()
        await db.refresh(project)

        return ProjectResponseSchema.model_validate(project)

    @staticmethod
    @exceptions
    async def create_feedback_project(
        project_id: int, feedback_data: FeedbackCreateSchema, db: AsyncSession
    ) -> ProjectResponseSchema:
        """
        Create a new feedback entry for a project.

        Args:
            project_id (int): The ID of the project to add feedback to.
            feedback_data (FeedbackCreateSchema): The feedback content.
            db (AsyncSession): The database session.
        Returns:
            ProjectResponseSchema: The updated project entry with the new feedback.
        """
        result = await db.execute(
            select(Project)
            .options(selectinload(Project.feedbacks))
            .where(Project.id == project_id)
        )
        project = result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"Project with ID {project_id} not found.",
            )

        # Create a new feedback entry
        new_feedback = Feedback(**feedback_data.model_dump(), project_id=project_id)
        db.add(new_feedback)
        await db.commit()
        await db.refresh(project)

        return ProjectResponseSchema.model_validate(project)

    @staticmethod
    @exceptions
    async def get_projects(db: AsyncSession) -> list[ProjectResponseSchema]:
        """
        Retrieve all project entries.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[ProjectResponseSchema]: A list of all project entries.
        """
        result = await db.execute(
            select(Project).options(selectinload(Project.feedbacks))
        )
        projects = result.scalars().all()
        return [ProjectResponseSchema.model_validate(project) for project in projects]

    @staticmethod
    @exceptions
    async def get_project_by_search(
        search_term: str, offset: int | None, limit: int | None, db: AsyncSession
    ) -> list[ProjectResponseSchema]:
        """
        Retrieve project entries that match the search term.

        Args:
            search_term (str): The term to search for in project names and descriptions.
            offset (int | None): The number of records to skip.
            limit (int | None): The maximum number of records to return.
            db (AsyncSession): The database session.
        Returns:
            List[ProjectResponseSchema]: A list of project entries that match the search term.
        """
        result = await db.execute(
            select(Project)
            .options(selectinload(Project.feedbacks))
            .where(
                (Project.nome.ilike(f"%{search_term}%"))
                | (Project.descricao.ilike(f"%{search_term}%"))
            )
            .offset(offset)
            .limit(limit)
        )
        projects = result.scalars().all()
        return [ProjectResponseSchema.model_validate(project) for project in projects]
