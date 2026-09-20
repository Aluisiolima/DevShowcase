from pydantic import BaseModel, ConfigDict, Field


class BaseSchemas(BaseModel):
    """Base class for all schemas."""

    model_config = ConfigDict(extra="ignore", from_attributes=True)
