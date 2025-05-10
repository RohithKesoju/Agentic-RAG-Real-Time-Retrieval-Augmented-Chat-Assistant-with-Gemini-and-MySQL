import json
import asyncio
import aiomysql
from database.mysql_connection import get_mysql_pool

async def process_data():
    with open("data_pipeline/raw_data.json", "r") as f:
        documents = json.load(f)

    pool = await get_mysql_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            for doc in documents:
                await cur.execute("""
                    REPLACE INTO executive_documents (id, title, summary, president, publication_date)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    doc['document_number'],
                    doc['title'],
                    doc.get('abstract', ''),
                    doc.get('president', ''),
                    doc['publication_date']
                ))
            await conn.commit()

if __name__ == "__main__":
    asyncio.run(process_data())
