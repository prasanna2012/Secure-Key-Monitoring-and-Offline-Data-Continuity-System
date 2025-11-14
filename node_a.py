# node_a.py  (Primary Node)
import socket
import threading

# Backup node info
BACKUP_HOST = '127.0.0.1'
BACKUP_PORT = 6001

clients = []
messages = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                messages.append(msg)

                # Broadcast to all connected clients
                for c in clients:
                    if c != client_socket:
                        c.send(msg.encode())

                # Send to backup
                send_to_backup(msg)

        except:
            if client_socket in clients:
                clients.remove(client_socket)
            client_socket.close()
            break

def send_to_backup(msg):
    try:
        backup = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backup.connect((BACKUP_HOST, BACKUP_PORT))
        backup.send(msg.encode())
        backup.close()
    except:
        print("⚠️ Backup node not reachable")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 6000))
    server.listen()
    print("Node A (Primary) running on port 6000...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
