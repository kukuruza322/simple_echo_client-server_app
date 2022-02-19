import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 20000
s.bind((IP, PORT))  # Bind the socket to address. The socket must not already be bound.
s.listen(1)  # Enable a server to accept connections. 1 - maximum of connections permit
connection, address = s.accept()
connection.send("Hi, you are welcome to connect and join to us!".encode('utf8'))  # send a greetings to client

with connection:
    print('Connected by ' + str(address))  # WTF is address[1] ???
    data_output = ''
    while True:
        data = connection.recv(2048).decode("utf8")
        data_output += data
        if not data:
            break
    print(data_output)