import socket

host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))

sock.listen(1)
print("The server is running and listening to client request")
conn, address = sock.accept()

message = "There is a message for you"
conn.send(message.encode())

conn.close()