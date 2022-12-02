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
# Continuously receive data from server
while True:
    data = s.recv(1024)
    print(f"\n{data.decode()}")
    # Check if data contains the word "Choice:"
    if "Choice:" in data.decode():
        choice = input("Enter your choice: ")
        s.send(choice.encode())

s.close()
