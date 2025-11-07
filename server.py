import socket
import os

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

print("🔌 Server is listening on port 8000...")

c, addr = s.accept()
print(f"✅ Client connected from {addr}")

while True:
    hostname = c.recv(1024).decode()
    print(f"🌍 Received hostname to ping: {hostname}")

    try:
        # System-level ping using 'os.popen'
        result = os.popen(f"ping -n 4 {hostname}").read()
        c.send(result.encode())

    except Exception as e:
        c.send(f"Ping failed: {str(e)}".encode())