from devshowcase.core import BaseModels
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from devshowcase.core.repository import Profile, Feedback, TechnologyProject


class Project(BaseModels):
    """
    Project model class
    """

    __tablename__ = "project"

    nome: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=False)
    curtidas: Mapped[int] = mapped_column(nullable=False, default=0)

    feedbacks: Mapped[list["Feedback"]] = relationship(
        "Feedback", back_populates="project", cascade="all, delete-orphan"
    )

    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"), nullable=False)

    profile: Mapped["Profile"] = relationship("Profile", back_populates="projects") 
    technology_projects: Mapped["TechnologyProject"] = relationship("TechnologyProject", back_populates="project")
