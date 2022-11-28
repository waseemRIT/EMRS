import socket
import os, sys, stat
import threading

# DEFINING CONSTANTS
USER = "waseem"
PASSWD = "password"
UNICODETYPE = "utf-8"


class Request(threading.Thread):
    def __init__(self, soc, address):
        threading.Thread.__init__(self)
        self.sock = soc
        self.add = address

    def run(self):
        self.start_request()

    def start_request(self):
        while True:
            print(f"Connecting with {str(self.add)}")
            request = self.sock.recv(2024)
            msg = request.decode("utf-8")

            if "waseem" in msg:
                print("Waseem is in the msg")

            if msg == "done":
                self.sock.close()

    def is_valid(self, username, password):
        if USER == username and PASSWD == password:
            return True
        else:
            return False


def client_request(connection, addr):
    print("Starting server")
    while True:
        msg = connection.recv(1024).decode("utf-8")
        print(msg)


def main():
    # server set up
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = socket.gethostname()
    port = 9999
    serversocket.bind((server_address, port))
    serversocket.listen()
    clients = []
    # starting to receive requests
    while True:
        connection, addr = serversocket.accept()
        client_connection = threading.Thread(target=client_request, args=(connection, addr))
        client_connection.start()


if __name__ == '__main__':
    main()
