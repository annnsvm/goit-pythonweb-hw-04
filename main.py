import argparse
import asyncio
from pathlib import Path
from utils import read_folder
from app_logger import logger


def parse_arguments():
    parser = argparse.ArgumentParser(description="Async file sorter")
    parser.add_argument("source", type=str, help="Source folder path")
    parser.add_argument("destination", type=str, help="Destination folder path")
    return parser.parse_args()

async def main():
    args = parse_arguments()
    source_path = Path(args.source)
    destination_path = Path(args.destination)

    if not source_path.exists() or not source_path.is_dir():
        logger.error("Source folder does not exist or is not a directory.")
        return

    destination_path.mkdir(parents=True, exist_ok=True)
    await read_folder(source_path, destination_path)

if __name__ == "__main__":
    asyncio.run(main())