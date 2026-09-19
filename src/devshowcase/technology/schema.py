from pydantic import Field
from devshowcase.core import BaseSchemas


class TechnologyCreateSchema(BaseSchemas):
    """
    Technology schema Create class
    """

    nome: str = Field(..., description="Technology name")
    descricao: str = Field(..., description="Technology description")


class TechnologyUpdateSchema(BaseSchemas):
    """
    Technology schema Update class
    """

    nome: str = Field(..., description="Technology name")
    descricao: str = Field(..., description="Technology description")


class TechnologyResponseSchema(BaseSchemas):
    """
    Technology schema Response class
    """

    nome: str
    descricao: str
