from __future__ import annotations

import asyncio

from .app import app


@app.task(queue="sums")
async def sum(a, b):
    return a + b


@app.task(queue="defer")
async def defer():
    await sum.defer_async(a=1, b=2)


@app.task(queue="count")
async def count():
    for i in range(20):
        print(i)
        await asyncio.sleep(1)
