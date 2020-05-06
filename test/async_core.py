import asyncio
from aiohttp import ClientSession


async def _send(url, session, http_type, headers, data):
    """
    Асинхронно отправляет запрос, не менее асинхронно читает ответ
    """
    if http_type == 'GET':
        async with session.get(url, headers=headers) as response:
            date = response.headers.get("date")
            print(f'{date}:{response.url}  {response.status}')
            return await response.read()
    elif http_type == 'POST':
        async with session.post(url, headers=headers, data=data) as response:
            return await response.read()


async def run(url, amount, http_type='GET', headers={}, data={}):
    """
    Формирует массив запросов, для последующего асинхронного вызова. 
    Выводит общий ответ всех вызовов
    """
    tasks = []
    async with ClientSession() as session:
        for _ in range(amount):
            task = asyncio.ensure_future(_send(url, session, http_type=http_type, headers=headers, data=data))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # print(responses)
