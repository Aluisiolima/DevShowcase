from devshowcase.core import BaseModels
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from devshowcase.core.repository import Project


class Profile(BaseModels):
    """
    Profile model class
    """

    __tablename__ = "profile"

    nome: Mapped[str] = mapped_column(nullable=False, unique=True)
    projects: Mapped[list["Project"]] = relationship(
        "Project", back_populates="profile", cascade="all, delete-orphan"
    )
