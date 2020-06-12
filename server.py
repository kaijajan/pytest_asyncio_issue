import asyncio
import pickle

class SimpleServer:
    def __init__(self, reader, writer):
        self.token = ''

        self.reader = reader
        self.writer = writer

        self.run = True

    async def client_handler(self):
        print('client_handler')
        count = 0
        while self.run and count < 10:
            print('receiving')
            data= await self.receive()
            print(f"data: {data}")
            if data:
                print('client_handler', data)
                await self.send(f'{data} returned')
                count += 1
            else:
                print('await 0.1')
                await asyncio.sleep(.1)

    async def send(self, data):
        if self.writer:
            binary = pickle.dumps(data)
            print(binary)
            self.writer.write(binary)
            print('sent')

    async def receive(self, size=1024):
        ret = None

        if self.reader:
            tmp = await self.reader.read(size)
            ret = pickle.loads(tmp)

        return ret

async def handle_client(reader, writer):
    print('handle_client')
    server = SimpleServer(reader, writer)
    await server.client_handler()


async def main():
    server = await asyncio.start_unix_server(handle_client, './server.sock')
    await server.serve_forever()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.close()


if __name__ == '__main__':
    asyncio.run(main())
