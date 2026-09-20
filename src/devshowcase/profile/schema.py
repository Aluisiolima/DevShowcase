from pydantic import Field
from devshowcase.core import BaseSchemas


class ProfileCreateSchema(BaseSchemas):
    """
    Profile schema Create class
    """

    nome: str = Field(..., description="Profile name")


class ProfileUpdateSchema(BaseSchemas):
    """
    Profile schema Update class
    """

    nome: str = Field(..., description="Profile name")


class ProfileResponseSchema(BaseSchemas):
    """
    Profile schema Response class
    """
    id:int
    nome: str
