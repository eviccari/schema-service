from fastapi import FastAPI
from .entrypoints.http_routers import validate_schema

app = FastAPI()
app.include_router(validate_schema.router)
