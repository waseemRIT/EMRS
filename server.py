import socket
import threading

# DEFINING CONSTANTS
USER = "waseem"
PASSWD = "password"
FORMAT = "utf-8"


def is_username_valid(username):
    if USER == username:
        return True
    else:
        return False


def is_password_valid(passwd):
    if passwd == PASSWD:
        return True
    else:
        return False


def client_request(my_socket, addr):
    # TODO: ONE ERROR EITHER TO BE FIXED OR REMOVED IS THE WHILE THAT KEEPS ASKING THE USER FOR USERNAME-PASSWORD
    print("Got a connection from %s" % str(addr))

    while True:
        username_req = "Insert Username: "
        my_socket.send(username_req.encode(FORMAT))
        req = my_socket.recv(2024)
        client_username = req.decode("utf-8")
        if is_username_valid(client_username):
            while True:
                password_req = "Insert Password: "
                my_socket.send(password_req.encode(FORMAT))
                req = my_socket.recv(2024)
                client_passowrd = req.decode("utf-8")
                if is_password_valid(client_passowrd):
                    while True:
                        req = my_socket.recv(2024)
                        option = req.decode("utf-8")
                        # TODO ADD SOME OPTIONS, SINCE WE HAVE TIME WE CAN DO COOL STUFF HERE, IF WE DO COOL STUFF WE
                        #  JUST EDIT THE IS_VALID FUNCTIONS
                        if option == "doctor":
                            pass
                        elif option == "disease":
                            pass
                        elif option == "bills":
                            pass
                        elif option == "done":
                            break

                    my_socket.close()
                else:
                    my_socket.send("Invalid Password!".encode(FORMAT))
        else:
            my_socket.send("Invalid Username!".encode(FORMAT))


def main():
    # server set up
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = socket.gethostname()
    port = 9999
    serversocket.bind((server_address, port))
    serversocket.listen()

    # starting to receive requests
    while True:
        sock, addr = serversocket.accept()
        client_connection = threading.Thread(target=client_request, args=(sock, addr))
        client_connection.start()


if __name__ == '__main__':
    main()
