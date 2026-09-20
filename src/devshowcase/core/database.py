from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from devshowcase.core.settings import Settings


class PostgresDB:
    def __init__(self):
        self.database_url = Settings().DATABASE_URL
        self.engine = create_async_engine(
            url=self.database_url, echo=not Settings().IS_PRODUCTION
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def get_session(self):
        """Get a new database session."""
        async with self.session_factory() as session:
            yield session


db = PostgresDB()
