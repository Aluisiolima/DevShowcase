from fastapi import FastAPI
from devshowcase.router import router
from devshowcase.core.settings import Settings


class DevShowcaseApp(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.router = router
        self.title = Settings().NAME_PROJECT
        self.description = Settings().DESCRIPTION
        self.version = Settings().VERSION
        self.docs_url = "/docs"
        self.redoc_url = "/redoc"

app = DevShowcaseApp()
