# Group Members:
# 1. Muaz Osman
# 2. Waseem Qaffaf
# 3. Kassem Darawcha
# 4. Muneer Alremawi

import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))
except socket.error as e:
    print(str(e))
    
# Send username and password to server
username = input("Enter username: ")
s.send(username.encode())
password = input("Enter password: ")
s.send(password.encode())
# Continuously receive data from server
while True:
    data = s.recv(1024)
    print(data.decode())
    # Check if data contains the word "Choice:"
    if "Choice:" in data.decode():
        choice = input()
        s.send(choice.encode())
    elif "Exiting" in data.decode():
        break
    elif "invalid username" in data.decode():
        break

s.close()
