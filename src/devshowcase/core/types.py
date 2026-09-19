from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from devshowcase.core.database import PostgresDB

AsyncSessionDep = Annotated[AsyncSession, Depends(PostgresDB.get_session)]
