from fastapi import FastAPI
from time import sleep
import asyncio

app = FastAPI()

@app.get("/sleep/sys")
def nsync_sys():
    sleep(1)
    return {"error":None}

@app.get("/sleep/async-sys")
async def async_sys():
    sleep(1)
    return {"error":None}

@app.get("/sleep/async-await")
async def async_async():
    await asyncio.sleep(1)
    return {"error":None}