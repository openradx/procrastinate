from __future__ import annotations

import time

from .app import app


@app.task(queue="sums")
def sum(a, b):
    print(f"{a} + {b} = {a + b}")


@app.task(queue="defer")
def defer():
    sum.defer(a=1, b=2)


@app.task(queue="count")
def count():
    for i in range(20):
        print(i)
        time.sleep(1)
