from devshowcase.core import BaseModels
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Feedback(BaseModels):
    """
    Feedback model class
    """

    __tablename__ = "feedback"

    text: Mapped[str] = mapped_column(nullable=False)
    estrela: Mapped[int] = mapped_column(nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"), nullable=False)
