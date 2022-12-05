# Group Members:
# 1. Muaz Osman
# 2. Waseem Qaffaf
# 3. Kassem Darawcha
# 4. Muneer Alremawi

import socket
try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Specifying type of connection like TCP
    host = socket.gethostname() # gets the  address of client machine used to connect later on
    port = 9999 # 9999 is the communication port between client and server
    s.connect((host, port)) # connects the client with the server
except socket.error:
    print("Connection Error")
    # End the program
    exit()

# Send username and password to server
username = input("Enter username: ")
# Send username to server
s.send(username.encode())
password = input("Enter password: ")
# Send password to server
s.send(password.encode())
# Continuously receive data from server
while True:
    data = s.recv(1024)     # used to received and store  the data
    print(data.decode())    # printing the received data
    # Check if data contains the word "Choice:"
    if "Choice:" in data.decode():
        choice = input()    # takes the specified option from client
        s.send(choice.encode())     # if choice is in server msg then the menu of options is sent
    elif "Exiting" in data.decode():    # If Existing comes from the servers msg then client has requested to exit
        break
    elif "invalid Username or Password" in data.decode():   # To Exit after notifying user that username/password is
        break # Invalid

s.close()   # to close the socket between client and server
