import logging
from logging import Logger
from pathlib import Path

import aiofiles
from fastapi import APIRouter, File, UploadFile

from fastpypi.config import settings

logger: Logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/package")
async def add_package(f: UploadFile = File(...)):

    package, _ = f.filename.rsplit("-", 1)
    d = Path(f"{settings.repo_dir}/{package}")
    logger.debug("mkdir %s", d)
    d.mkdir(parents=True, exist_ok=True)

    async with aiofiles.open(f"{d}/{f.filename}", mode="wb") as p:
        # TODO: not efficent for large files
        await p.write(f.file.read())

    logger.debug("created package %s/%s", d.name, f.filename)
    return f"{package}/{f.filename}"
