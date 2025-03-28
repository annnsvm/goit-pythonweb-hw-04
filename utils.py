import asyncio
import aiofiles
from app_logger import logger
from pathlib import Path

async def copy_file(file_path: Path, dest_folder: Path):
    try:
        ext = file_path.suffix[1:] if file_path.suffix else "unknown"
        target_folder = dest_folder / ext
        target_folder.mkdir(parents=True, exist_ok=True)
        dest_file_path = target_folder / file_path.name

        async with aiofiles.open(file_path, "rb") as src, aiofiles.open(dest_file_path, "wb") as dest:
            await dest.write(await src.read())

        logger.info(f"Copied {file_path} -> {dest_file_path}")
    except Exception as e:
        logger.error(f"Error copying {file_path}: {e}")

async def read_folder(source_folder: Path, dest_folder: Path):
    tasks = []
    for file_path in source_folder.rglob("*"):
        if file_path.is_file():
            tasks.append(copy_file(file_path, dest_folder))
    await asyncio.gather(*tasks)