import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())  # check this before run if client-server are not in one PC.
PORT = 20000
connection.connect((IP, PORT))
read_server_repsonse = connection.recv(2048)
print(read_server_repsonse.decode('utf8'))
connection.send("Well done!".encode('utf8'))  # return a greetings message to server when connection starts.
connection.close()  # close connection after message
