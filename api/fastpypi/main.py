# type: ignore[attr-defined]
import logging
from logging import Logger

from fastapi import FastAPI

from fastpypi.config import settings
from fastpypi.middleware import setup_middleware
from fastpypi.router import api_router

logger: Logger = logging.getLogger(__name__)

api = FastAPI(debug=True, root_path=settings.root_path)
setup_middleware(api)
api.include_router(api_router, prefix=settings.api_v1_str)


def print_debug_routes() -> None:
    max_len = max(len(route.path) for route in api.routes)
    routes = sorted(
        [
            (method, route.path, route.name)
            for route in api.routes
            for method in getattr(route, "methods", None) or ["WS"]
        ],
        key=lambda x: (x[1], x[0]),
    )
    route_table = "\n".join(f"{method:7} {path:{max_len}} {name}" for method, path, name in routes)
    logger.debug(f"Route Table:\n{route_table}")


@api.on_event("startup")
async def startup_event() -> None:
    logger.info("startup")
    logger.debug(settings)
    print_debug_routes()


@api.on_event("shutdown")
def shutdown_event() -> None:
    logger.debug("shutdown")
