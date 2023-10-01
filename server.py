import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print('Server is listening.')

conn, addr = server.accept()
connection=True

while connection:
    message_len = conn.recv(HEADER).decode(FORMAT)
    if message_len:
        message_len = int(message_len)
        message = conn.recv(message_len).decode(FORMAT)
        if message == DISCONNECT_MESSAGE:
                connection =  False
                conn.send('Connection Closed.'.encode(FORMAT))
        else:
            c=0
            for i in message:
                if i in "aeiouAEIOU":
                    c+=1
            
            if c==0:
                conn.send("Not enough vowels".encode(FORMAT))
            elif c<=2:
                conn.send("Enough vowels I guess".encode(FORMAT))
            else:
                conn.send("Too many vowels".encode(FORMAT))
            conn.send('Message Received.'.encode(FORMAT))
conn.close()