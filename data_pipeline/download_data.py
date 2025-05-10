import aiohttp
import asyncio
import json
from datetime import datetime, timedelta

async def download_data():
    async with aiohttp.ClientSession() as session:
        today = datetime.now()
        start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
        url = f"https://api.fda.gov/drug/event.json?search=receivedate:[20240501+TO+20240510]&limit=100"
        
        async with session.get(url) as resp:
            data = await resp.json()
            with open("data_pipeline/raw_data.json", "w") as f:
                json.dump(data['results'], f)

if __name__ == "__main__":
    asyncio.run(download_data())