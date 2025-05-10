import asyncio
from data_pipeline.download_data import download_data
from data_pipeline.process_data import process_data

async def main():
    await download_data()
    await process_data()

if __name__ == "__main__":
    asyncio.run(main())
