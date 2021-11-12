import httpx
import asyncio


API_REQUEST_URL="https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback"

async def request(client,cashback, document):
    print(cashback, document)
    response = await client.post(API_REQUEST_URL)
    return response.text


async def task(cashback, document):
    async with httpx.AsyncClient() as client:
        tasks = [request(client=client, cashback=cashback, document=document) for i in range(100)]
        result = await asyncio.gather(*tasks)
        return result
