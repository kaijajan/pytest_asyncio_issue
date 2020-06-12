import asyncio
import pickle

class SimpleClient:
    def __init__(self):
        self.token = ''

        self.reader = None
        self.writer = None

        self.run = True
    
    async def connect(self, sock):
        self.reader, self.writer = await asyncio.open_unix_connection(sock)

    async def send(self, data):
        if self.writer:
            binary = pickle.dumps(data)
            self.writer.write(binary)

    async def receive(self, size=1024):
        ret = None

        if self.reader:
            tmp = await self.reader.read(size)
            ret = pickle.loads(tmp)

        return ret



async def main():
    run = 0

    client = SimpleClient()
    await client.connect('./server.sock')

    for i in range(10):
        await client.send(f'hello {i}')
        data = await client.receive()
        print(f'received: {data}')
        await asyncio.sleep(.1)
        i += 1

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
