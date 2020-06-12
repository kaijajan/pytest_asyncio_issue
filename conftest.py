import pytest
import asyncio
from client import SimpleClient

def pytest_configure(config):
    pytest.client = None

def pytest_sessionstart(session):
    pass


def pytest_sessionfinish(session):
    pass
    # if pytest.client:
    #     pytest.client.close()

@pytest.fixture(scope='session')
async def client(request):
    print('client init')
    client = SimpleClient()
    print('connecting')
    await client.connect('./server.sock')
    print('connected, yielding')
    yield client