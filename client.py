import asyncio

class SimpleClient:
    def __init__(self):
        self.reader = None
        self.writer = None

    async def connect(self, sock):
        self.reader, self.writer = await asyncio.open_unix_connection(sock)
        # self.reader, self.writer = await asyncio.open_connection(*sock)

    async def send(self, data):
        binary = data.encode()
        self.writer.write(binary)
        await self.writer.drain()

    async def receive(self, size=1024):
        binary = await self.reader.read(size)
        if not binary:
            return None
        return binary.decode()

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()


