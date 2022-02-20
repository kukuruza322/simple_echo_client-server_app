import socket
from time import localtime, strftime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 20000
s.bind((IP, PORT))  # Bind the socket to address. The socket must not already be bound.
s.listen(1)  # Enable a server to accept connections. 1 - maximum of connections permit
connection, address = s.accept()


class User:
    def __init__(self, name, message=""):
        self.name = name
        self.message = message


with connection:
    connection.send("Hi! You are welcome to join us!".encode('utf8'))  # send a greetings to client
    getting_username = connection.recv(2048).decode("utf8")
    user = User(getting_username)
    greetings = user.name + ' enter chat. ' + 'Connected by ' + str(address[0]) + '.'
    print(greetings)  # WTF is address[1] ???
    connection.send(greetings.encode('utf8'))

    while True:
        input_message = connection.recv(2048).decode("utf8")
        user.message = input_message
        processed_message = str('[' + strftime("%H:%M:%S", localtime()) + '] ' + user.name + ': ' + user.message)
        connection.send(processed_message.encode('utf8'))
        print(processed_message)
        if not input_message:
            break

