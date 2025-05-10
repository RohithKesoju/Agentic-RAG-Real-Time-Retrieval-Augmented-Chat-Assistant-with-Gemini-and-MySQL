import aiomysql

from database.mysql_connection import get_mysql_pool

async def query_executive_orders(president: str, month: str):
    pool = await get_mysql_pool()
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute("""
                SELECT title, summary FROM executive_documents
                WHERE president LIKE %s AND MONTH(publication_date) = %s
                ORDER BY publication_date DESC
            """, (f"%{president}%", int(month)))
            return await cur.fetchall()
