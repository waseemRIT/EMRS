import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.connect((host, port))

# Send username and password to server
username = input("Enter username: ")
s.send(username.encode())
password = input("Enter password: ")
s.send(password.encode())
# Receive data from server
while True:
    data = s.recv(1024)
    if not data:
        break
    print(data.decode())

