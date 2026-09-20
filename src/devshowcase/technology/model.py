from devshowcase.core import BaseModels
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from devshowcase.project.model import Project


class Technology(BaseModels):
    """
    Technology model class
    """

    __tablename__ = "technology"

    nome: Mapped[str] = mapped_column(nullable=False, unique=True)
    descricao: Mapped[str] = mapped_column(nullable=False)

    technology_projects: Mapped[list["TechnologyProject"]] = relationship(
        "TechnologyProject", back_populates="technology", cascade="all, delete-orphan"
    )


class TechnologyProject(BaseModels):
    """
    TechnologyProject model class
    """

    __tablename__ = "technology_project"

    technology_id: Mapped[int] = mapped_column(
        ForeignKey("technology.id"), nullable=False
    )
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"), nullable=False)

    technology: Mapped["Technology"] = relationship(
        "Technology", back_populates="technology_projects"
    )
    project: Mapped["Project"] = relationship(
        "Project", back_populates="technology_projects"
    )
