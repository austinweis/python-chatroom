import socket

HOST = "127.0.0.1"
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    name = input("enter a username: ")
    while True:
        message = input("send a message: ")
        s.sendall(message.encode("UTF-8"))
        data = s.recv(1024)

        print(data.decode("UTF-8"))