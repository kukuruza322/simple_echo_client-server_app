import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())  # check this before run if client-server are not in one PC.
PORT = 20000
connection.connect((IP, PORT))
read_server_response = connection.recv(2048)  # get and print a hello message from server
print(read_server_response.decode('utf8'))
message = input("Enter you nickname and Press Enter: ")
connection.send(message.encode('utf8'))
print("Welcome, " + message + "!")

while True:
    message = input('Enter your text: ')
    if message == "exit":
        connection.close()  # close connection after EXIT code
        break
    connection.send(message.encode('utf8'))
    read_server_response = connection.recv(2048)
    print(read_server_response.decode('utf8'))
