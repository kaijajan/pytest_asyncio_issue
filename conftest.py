import pytest
import asyncio
from client import SimpleClient


@pytest.fixture(scope='session')
async def client():
    print('client init')
    client = SimpleClient()
    print('connecting')
    # await client.connect('./server.sock')
    await client.connect(('127.0.0.1',5062))
    print('connected, yielding')
    yield client
    await client.close()


@pytest.fixture(scope="session")
def event_loop():
    """Change event_loop fixture to module level."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
