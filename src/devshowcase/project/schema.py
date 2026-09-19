from pydantic import Field
from devshowcase.core import BaseSchemas
from devshowcase.technology.schema import (
    TechnologyResponseSchema,
    TechnologyCreateSchema,
)


class ProjectCreateSchema(BaseSchemas):
    """
    Project schema Create class
    """

    nome: str = Field(..., description="Project name")
    descricao: str = Field(..., description="Project description")
    tecnologias: list[TechnologyCreateSchema] = Field(
        ..., description="List of technology names associated with the project"
    )


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

    nome: str
    descricao: str
    tecnologias: list[TechnologyResponseSchema]
