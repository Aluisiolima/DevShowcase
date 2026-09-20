from fastapi import APIRouter


from devshowcase.project.controller import project_router
from devshowcase.technology.controller import technology_router
from devshowcase.feedback.controller import feedback_router
from devshowcase.profile.controller import profile_router

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Welcome to the Dev Showcase API!"}


router.include_router(project_router)
router.include_router(technology_router)
router.include_router(feedback_router)
router.include_router(profile_router)
