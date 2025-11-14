# node_b.py  (Backup Node)
import socket

messages = []

def start_backup_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 6001))
    server.listen()
    print("Node B (Backup) running on port 6001...")

    while True:
        client_socket, addr = server.accept()
        msg = client_socket.recv(1024).decode()
        messages.append(msg)

        print("Backup received:", msg)

        client_socket.close()

if __name__ == "__main__":
    start_backup_server()
