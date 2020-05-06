from time import time
import asyncio

from async_core import run
from config import TEST_URL, AMOUNT_REQUESTS


if __name__ == "__main__":

    start = time()

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(TEST_URL, AMOUNT_REQUESTS))
    loop.run_until_complete(future)

    print(time() - start)
