from http import HTTPStatus

from fastapi import APIRouter
from devshowcase.core.types import AsyncSessionDep
from devshowcase.technology.service import TechnologyService
from devshowcase.technology.schema import (
    TechnologyCreateSchema,
    TechnologyResponseSchema,
)

technology_router = APIRouter(prefix="/technology", tags=["Technology"])


@technology_router.post(
    "/", response_model=TechnologyResponseSchema, status_code=HTTPStatus.CREATED
)
async def create_technology(
    technology: TechnologyCreateSchema, session: AsyncSessionDep
) -> TechnologyCreateSchema:
    return await TechnologyService.create_technology(technology_data=technology, db=session)


@technology_router.get(
    "/", response_model=list[TechnologyResponseSchema], status_code=HTTPStatus.OK
)
async def get_all_technologies(
    session: AsyncSessionDep,
) -> list[TechnologyResponseSchema]:
    return await TechnologyService.get_technologys(db=session)
