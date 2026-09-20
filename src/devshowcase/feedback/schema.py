from pydantic import Field

from devshowcase.core import BaseSchemas


class FeedbackCreateSchema(BaseSchemas):
    """
    Feedback schema Create class
    """

    text: str = Field(..., description="Feedback text")
    estrela: int = Field(..., description="Feedback star rating", ge=1, le=5)


class FeedbackUpdateSchema(BaseSchemas):
    """
    Feedback schema Update class
    """

    text: str = Field(..., description="Feedback text")
    estrela: int = Field(..., description="Feedback star rating", ge=1, le=5)


class FeedbackResponseSchema(BaseSchemas):
    """
    Feedback schema Response class
    """

    id: int
    text: str
    estrela: int
