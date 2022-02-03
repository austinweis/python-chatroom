import socket, selectors

HOST = "127.0.0.1"
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("starting server...")
    s.bind((HOST, PORT))
    print("binding socket to host...")
    s.listen()
    print("listening on port...\n")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            conn.sendall(b"message received")
            if data.decode("UTF-8") == "close":
                print("closing...")
                break