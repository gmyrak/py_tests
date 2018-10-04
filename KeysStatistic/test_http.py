import socket

sock = socket.socket()
sock.bind(('', 8181))
sock.listen(10)

while True:
    print('Wait accept...')
    conn, addr = sock.accept()
    print("New connection from {}".format(addr))
    data = conn.recv(2048).decode()
    print(data)
    try:
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        conn.send(b"Hello!\r\n")
    except Exception:
        print("Can't sendanswer")


