from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database import create_tables, drop_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('dropping tables')
    await create_tables()
    print('created tables')
    yield
    print('restarting app')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

if __name__ == '__main__':
    uvicorn.run(app, host='192.168.0.110', port=8000)
