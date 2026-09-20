from http import HTTPStatus

from fastapi import APIRouter
from devshowcase.project.service import ProjectService
from devshowcase.project.schema import (
    ProjectCreateSchema,
    ProjectResponseSchema,
)

from devshowcase.feedback.schema import FeedbackCreateSchema

from devshowcase.core.types import AsyncSessionDep

project_router = APIRouter(prefix="/project", tags=["Project"])


@project_router.post(
    "/", response_model=ProjectResponseSchema, status_code=HTTPStatus.CREATED
)
async def create_project(
    project: ProjectCreateSchema, session: AsyncSessionDep
) -> ProjectCreateSchema:
    return await ProjectService.create_project(project_data=project, db=session)


@project_router.get(
    "/{id}", response_model=ProjectResponseSchema, status_code=HTTPStatus.CREATED
)
async def get_project(id: int, session: AsyncSessionDep) -> ProjectResponseSchema:
    return await ProjectService.get_project_by_id(id=id, db=session)


@project_router.put(
    "/{id}", response_model=ProjectResponseSchema, status_code=HTTPStatus.CREATED
)
async def add_curtida_project(
    id: int, session: AsyncSessionDep
) -> ProjectResponseSchema:
    return await ProjectService.add_curtida_project(project_id=id, db=session)


@project_router.post(
    "/{id}/feedback",
    response_model=ProjectResponseSchema,
    status_code=HTTPStatus.CREATED,
)
async def add_feedback_project(
    id: int, feedback: FeedbackCreateSchema, session: AsyncSessionDep
) -> ProjectResponseSchema:
    return await ProjectService.create_feedback_project(
        project_id=id, feedback_data=feedback, db=session
    )


@project_router.get(
    "/", response_model=list[ProjectResponseSchema], status_code=HTTPStatus.OK
)
async def get_all_projects(session: AsyncSessionDep) -> list[ProjectResponseSchema]:
    return await ProjectService.get_projects(db=session)


@project_router.get(
    "/search/{search_term}",
    response_model=list[ProjectResponseSchema],
    status_code=HTTPStatus.OK,
)
async def search_projects(
    search_term: str, offset: int | None, limit: int | None, session: AsyncSessionDep
) -> list[ProjectResponseSchema]:
    return await ProjectService.get_project_by_search(
        search_term=search_term, offset=offset, limit=limit, db=session
    )
