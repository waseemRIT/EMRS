import requests
import bs4
import socket
import threading

# DEFINING CONSTANTS
USER = "admin"
PASSWD = "password"
FORMAT = "utf-8"
LoginSuccess = False
headers = ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']


def get_azan_time():
    res = requests.get(r"https://www.khaleejtimes.com/prayer-time-uae/dubai")
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    azan_times = list()
    i = 1
    h = 0
    for x in range(5, 11):
        time = soup.select(
            f'body > div.wrapper > main > div.single.prayer-timing > div:nth-child(2) > div:nth-child(2) > '
            f'div.col-12.col-lg-9 > div:nth-child(4) > div > div.draft-rates-main-wrapper-nf > div > table > tbody > '
            f'tr:nth-child(1) > td:nth-child({x})')

        azan_times.append([headers[h], time[0].text.strip()])
        i += 1
        h += 1
    return azan_times


azan_time = get_azan_time()


def get_farj():
    fajr = azan_time[1][1]
    return f"Fajr Azan is at: {fajr}\n"


def get_Dhur():
    Dhur = azan_time[2][1]
    return f"Dhur Azan is at: {Dhur}\n"


def get_Asr():
    Asr = azan_time[3][1]
    return f"Asr Azan is at: {Asr}\n"


def get_Maghrib():
    Maghrib = azan_time[4][1]
    return f"Maghrib Azan is at: {Maghrib}\n"


def get_Isha():
    Isha = azan_time[5][1]
    return f"Isha Azan is at: {Isha}\n"


def client_request(my_socket, addr):
    # Print the address of the client that just connected
    print("Connection from: " + str(addr))
    # Receive the username input from the client
    username = my_socket.recv(1024).decode(FORMAT)
    # Receive the password from the client
    password = my_socket.recv(1024).decode(FORMAT)
    my_socket.send("Hi".encode(FORMAT))
    # Verify the username and password
    if username == USER and password == PASSWD:
        # Send an acknowledgement to the client
        LoginSuccess = True
        my_socket.send("\nLogin successful".encode(FORMAT))
    else:
        # Send an acknowledgement to the client
        LoginSuccess = False
        my_socket.send("\nLogin failed".encode(FORMAT))
    if LoginSuccess:
        my_socket.send("\nWelcome to the server\nThese are Dubai Timings\n".encode(FORMAT))
        while True:
            # Send a menu to the client
            # send a option to send Fajr Athan Timing
            my_socket.send("[1] Send Fajr Time\n".encode(FORMAT))
            # send a option to send Duhr Athan Timing
            my_socket.send("[2] Send Duhr Time\n".encode(FORMAT))
            # send a option to send Aser Athan Timing
            my_socket.send("[3] Send Aser Time\n".encode(FORMAT))
            # send a option to send Maghrib Athan Timing
            my_socket.send("[4] Send Maghrib Time\n".encode(FORMAT))
            # send a option to send Isha Athan Timing
            my_socket.send("[5] Send Isha Time\n".encode(FORMAT))
            # type done to exit
            my_socket.send("Type 'done' to exit\n".encode(FORMAT))
            # Receive the choices from the client
            my_socket.send("Enter your Choice: ".encode(FORMAT))
            choice = my_socket.recv(1024).decode(FORMAT)
            # Send the appropriate data to the client
            if choice == "1":
                my_socket.send(get_farj().encode(FORMAT))
                continue
            elif choice == "2":
                my_socket.send(get_Dhur().encode(FORMAT))
            elif choice == "3":
                my_socket.send(get_Asr().encode(FORMAT))
            elif choice == "4":
                my_socket.send(get_Maghrib().encode(FORMAT))
                continue
            elif choice == 5:
                my_socket.send(get_Isha().encode(FORMAT))
                continue
            elif choice == "done":
                my_socket.send("\nExiting".encode(FORMAT))
                my_socket.close()
    elif not LoginSuccess:
        my_socket.send("\n invalid username or password\nExiting...".encode(FORMAT))
        my_socket.close()


def main():
    # Create a socket object
    my_socket = socket.socket()
    # Get the hostname
    host = socket.gethostname()
    # Reserve a port for your service
    port = 9999
    # Bind to the port
    my_socket.bind((host, port))
    # Wait for client connection
    my_socket.listen(5)
    while True:
        # Establish connection with client
        c, addr = my_socket.accept()
        try:
            # Start a new thread and return its identifier
            t = threading.Thread(target=client_request, args=(c, addr))
            # Start new thread
            t.start()
        except  OSError:
            print("Client Force Stop")


if __name__ == "__main__":
    main()
