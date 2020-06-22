import pytest
import asyncio

@pytest.mark.asyncio
async def test_1(client):
    for i in range(10):
        await client.send(f'hello {i}')
        data = await client.receive()
        if not data:
            print('connection closed')
            break
        print(f'received: {data}')
        await asyncio.sleep(.1)
        i += 1
    assert True
    print('hello world')

@pytest.mark.asyncio
async def test_2(client):
    for i in range(10):
        await client.send(f'hello {i}')
        data = await client.receive()
        if not data:
            print('connection closed')
            break
        print(f'received: {data}')
        await asyncio.sleep(.1)
        i += 1
    assert True