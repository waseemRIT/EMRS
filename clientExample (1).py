import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.connect((host, port))
s.send("".encode("utf-8"))

while True:
    recieved =s.recv(2024)
    print (recieved.decode('utf-8'))

    reply = input("")
    s.send(reply.encode("utf-8"))