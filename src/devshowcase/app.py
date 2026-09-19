from fastapi import FastAPI
from devshowcase.router import router
from devshowcase.core.settings import Settings


app = FastAPI(
    title=Settings().NAME_PROJECT,
    description=Settings().DESCRIPTION,
    version=Settings().VERSION,
)

app.include_router(router, prefix=Settings().ROOT_PATH)
