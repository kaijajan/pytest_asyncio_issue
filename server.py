import asyncio


class SimpleServer:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    async def client_handler(self):
        count = 0
        while True:
            print(f'receiving {count}')
            data= await self.receive()
            if not data:
                break
            await self.send(f'{data} returned')
            count += 1

    async def send(self, data):
        binary = data.encode()
        self.writer.write(binary)
        await self.writer.drain()
        print(f'{binary} sent')

    async def receive(self, size=1024):
        binary = await self.reader.read(size)
        if not binary:
            return None
        return binary.decode()

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()


async def handle_client(reader, writer):
    print('handle_client')
    server = SimpleServer(reader, writer)
    await server.client_handler()
    print('end of handle_client')


async def main():
    server = await asyncio.start_unix_server(handle_client, './server.sock')
    # server = await asyncio.start_server(handle_client, '127.0.0.1', 5062)
    print("server waiting client connection")
    await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
