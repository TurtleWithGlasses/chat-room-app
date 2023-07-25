import socket
from threading import Thread

host = "127.0.0.1"
port = 8080
clients = {}
addresses = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))

def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, " has connected...")
        client_conn.send(" Welcome to the Chat Room. Please type your name to continue".encode("utf8"))
        addresses[client_conn] = client_address

if __name__ == "__main__":
    sock.listen(5)
    print("The server is running")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()