import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())  # check this before run if client-server are not in one PC.
PORT = 20000
connection.connect((IP, PORT))
print(connection.recv(2048).decode("utf8"))  # get and print a hello message from server
message = input("Enter you nickname and Press Enter: ")
connection.send(message.encode('utf8'))
print(connection.recv(2048).decode("utf8"))  # get and print a individual greetings from server

while True:
    message = input('Enter your text: ')
    # print("user : " + message) - works fine but only for 1 user. Проще делать обратную рассылку на всех активных пользователей
    # кто подключен, иначе в консоли будет дублирование локального сообщения и обработонного, полученного с сервера.
    if message == "exit":
        connection.close()  # close connection after EXIT code
        break
    connection.send(message.encode('utf8'))
    print(connection.recv(2048).decode("utf8"))
