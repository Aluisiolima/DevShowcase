from pydantic import Field
from devshowcase.core import BaseSchemas


class ProfileCreateSchema(BaseSchemas):
    """
    Profile schema Create class
    """

    nome: str = Field(..., description="Profile name")
    descricao: str = Field(..., description="Profile description")


class ProfileUpdateSchema(BaseSchemas):
    """
    Profile schema Update class
    """

    nome: str = Field(..., description="Profile name")
    descricao: str = Field(..., description="Profile description")


class ProfileResponseSchema(BaseSchemas):
    """
    Profile schema Response class
    """

    nome: str
    descricao: str
