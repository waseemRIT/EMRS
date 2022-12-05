# Group Members:
# 1. Muaz Osman
# 2. Waseem Qaffaf
# 3. Kassem Darawcha
# 4. Muneer Alremawi

import socket
try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get local machine name
    host = socket.gethostname()
    # Defining the Port.
    port = 9999
    # Connect to server
    s.connect((host, port))
except socket.error as e:
    # Print error message
    print(str(e))
    
# Send username and password to server
username = input("Enter username: ")
# Send username to server
s.send(username.encode())
password = input("Enter password: ")
# Send password to server
s.send(password.encode())
# Continuously receive data from server
while True:
    # Receive data from server
    data = s.recv(1024)
    # Print data
    print(data.decode())
    # Check if data contains the word "Choice:" then send user choice to server
    if "Choice:" in data.decode():
        choice = input()
        s.send(choice.encode())
    # Check if data contains the word "Exiting" then break
    elif "Exiting" in data.decode():
        break
    # Check if data contains the word "invalid username" then break
    elif "invalid username" in data.decode():
        break

s.close()
