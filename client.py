import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(message):
    message = message.encode(FORMAT)
    message_len = len(message)
    send_len = str(message_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))

    client.send(send_len)
    client.send(message)

    print(client.recv(1024).decode(FORMAT))
    print(client.recv(1024).decode(FORMAT))
    
    
while True:
    n = input("enter a word: ")
    if n =='Done':
        send_message(DISCONNECT_MESSAGE)
        break
    else:
        send_message(n)
