from fastapi import APIRouter

from fastpypi.routes import repo

api_router = APIRouter()
api_router.include_router(repo.router, prefix="/repo", tags=["Repo"])
