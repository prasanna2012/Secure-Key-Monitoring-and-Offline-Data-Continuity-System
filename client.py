# client.py  (Client Chat Program)
import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6000

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print("\nReceived:", msg)
        except:
            print("Disconnected from server.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    print("Connected to Node A (Primary Server)...")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input("You: ")
        client.send(msg.encode())

if __name__ == "__main__":
    start_client()
