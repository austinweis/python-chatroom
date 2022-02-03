#!/usr/bin/env python3

import socket, asyncio

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1234        # Port to listen on (non-privileged ports are > 1023)

connections = []

async def receive_data(conn):
    return conn.recv(1024)
async def client_handler():
    print("handle")
    for conn, addr in connections:
        with conn:
            print('Connected by', addr)
            while True:
                print("loop")
                data = await receive_data(conn)
                print(data)
                if not data:
                    break
                await conn.sendall(data)

async def client_listener():
    while True:
        print("listen")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            await connections.append(s.accept())

async def main():
    listen = asyncio.create_task(client_listener())
    handle = asyncio.create_task(client_handler())

    await listen
    await handle


asyncio.run(main())
