import socket

UNICODETYPE = "utf-8"
# Client Port Set up
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))

while True:
    option = input("Enter Msg:")
    message = option.encode(UNICODETYPE)

    s.send(message)
    if option == "done":
        print("Closing connection")
        break
