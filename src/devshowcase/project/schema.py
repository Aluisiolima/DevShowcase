from pydantic import Field
from devshowcase.core import BaseSchemas
from devshowcase.feedback.schema import (
    FeedbackResponseSchema,
)


class ProjectCreateSchema(BaseSchemas):
    """
    Project schema Create class
    """

    nome: str = Field(..., description="Project name")
    descricao: str = Field(..., description="Project description")
    profile_id: int = Field(..., description="Profile id")


class ProjectUpdateSchema(BaseSchemas):
    """
    Project schema Update class
    """

    nome: str = Field(..., description="Project name")
    descricao: str = Field(..., description="Project description")


class ProjectResponseSchema(BaseSchemas):
    """
    Project schema Response class
    """
    id: int
    nome: str
    descricao: str
    curtidas: int
    feedbacks: list[FeedbackResponseSchema]
