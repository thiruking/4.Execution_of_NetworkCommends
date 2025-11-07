import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    ip = input("Enter the website you want to ping: ")
    s.send(ip.encode())

    response = s.recv(4096).decode()
    print("Server Response:\n", response)
    print("-" * 60)