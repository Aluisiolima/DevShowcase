from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from devshowcase.core.database import db

AsyncSessionDep = Annotated[AsyncSession, Depends(db.get_session)]
