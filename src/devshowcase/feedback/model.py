from devshowcase.core import BaseModels
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from devshowcase.core.repository import Project


class Feedback(BaseModels):
    """
    Feedback model class
    """

    __tablename__ = "feedback"

    text: Mapped[str] = mapped_column(nullable=False)
    estrela: Mapped[int] = mapped_column(nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"), nullable=False)
    project: Mapped["Project"] = relationship(
        "Project", back_populates="feedbacks"
    )