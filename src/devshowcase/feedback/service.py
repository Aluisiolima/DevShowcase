from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from devshowcase.core.exceptions import exceptions
from devshowcase.core.repository import Feedback
from devshowcase.feedback.schema import FeedbackCreateSchema, FeedbackResponseSchema


class FeedbackService:
    """
    Service class for Feedback operations
    """

    @staticmethod
    @exceptions
    async def create_feedback(
        feedback_data: FeedbackCreateSchema, db: AsyncSession
    ) -> FeedbackResponseSchema:
        """
        Create a new feedback entry in the database.

        Args:
            feedback_data (FeedbackCreateSchema): The data for the new feedback.
            db (AsyncSession): The database session.

        Returns:
            FeedbackResponseSchema: The created feedback entry.
        """
        new_feedback = Feedback(**feedback_data.model_dump())
        db.add(new_feedback)
        await db.commit()
        await db.refresh(new_feedback)
        return FeedbackResponseSchema.model_validate(new_feedback)

    @staticmethod
    @exceptions
    async def get_feedbacks(db: AsyncSession) -> list[FeedbackResponseSchema]:
        """
        Retrieve all feedback entries from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            list[FeedbackResponseSchema]: A list of all feedback entries.
        """
        result = await db.execute(select(Feedback))
        feedbacks = result.scalars().all()
        return [
            FeedbackResponseSchema.model_validate(feedback) for feedback in feedbacks
        ]
