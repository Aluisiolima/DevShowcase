from fastapi import FastAPI
from .router import router


class DevShowcaseApp(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.router = router
        self.title = "Dev Showcase"
        self.description = "A showcase of development projects and tools."
        self.version = "1.0.0"
        self.docs_url = "/docs"
        self.redoc_url = "/redoc"


app = DevShowcaseApp()
