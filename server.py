import socket
import threading

# DEFINING CONSTANTS
USER = "waseem"
PASSWD = "password"
FORMAT = "utf-8"
LoginSuccess = False

# Medical Records
medical_records = ["Patient1", "Patient2", "Patient3", "Patient4", "Patient5"]
# Doctors
doctors = ["Doctor1", "Doctor2", "Doctor3", "Doctor4", "Doctor5"]
# Hospitals
hospitals = ["Hospital1", "Hospital2", "Hospital3", "Hospital4", "Hospital5"]
# Pharmacies
pharmacies = ["Pharmacy1", "Pharmacy2", "Pharmacy3", "Pharmacy4", "Pharmacy5"]

def client_request(my_socket, addr):
    #Print the address of the client that just connected
    print("Connection from: " + str(addr))
    #Recieve the username input from the client
    username = my_socket.recv(1024).decode(FORMAT)
    #Recieve the password from the client
    password = my_socket.recv(1024).decode(FORMAT)
    my_socket.send("Hi".encode(FORMAT))
    #Verify the username and password
    if username == USER and password == PASSWD:
        #Send an acknowledgement to the client
        LoginSuccess = True
        my_socket.send("\nLogin successful".encode(FORMAT))
    else:
        #Send an acknowledgement to the client
        LoginSuccess = False
        my_socket.send("\nLogin failed".encode(FORMAT))
    if LoginSuccess == True:
        #Send a menu to the client
        my_socket.send("\nWelcome to the server".encode(FORMAT))
        #send a option to send Medical Records
        my_socket.send("\n1. Send Medical Records".encode(FORMAT))
        #Send a option to send a list of doctors
        my_socket.send("\n2. Send a list of doctors".encode(FORMAT))
        #Send a option to send a list of hospitals
        my_socket.send("\n3. Send a list of hospitals".encode(FORMAT))
        #Send a option to send a list of pharmacies
        my_socket.send("\n4. Send a list of pharmacies".encode(FORMAT))
        #type done to exit
        my_socket.send("\nType 'done' to exit".encode(FORMAT))
        #Recieve the choices from the client
        my_socket.send("Enter your Choice: ".encode(FORMAT))
        choice = my_socket.recv(1024).decode(FORMAT)
        #Send the appropriate data to the client
        if choice == "1":
            my_socket.send("\nSending Medical Records".encode(FORMAT))
            for record in medical_records:
                my_socket.send(record.encode(FORMAT))
        elif choice == "2":
            my_socket.send("\nSending a list of doctors".encode(FORMAT))
            for doctor in doctors:
                my_socket.send(doctor.encode(FORMAT))
        elif choice == "3":
            my_socket.send("\nSending a list of hospitals".encode(FORMAT))
            for hospital in hospitals:
                my_socket.send(hospital.encode(FORMAT))
        elif choice == "4":
            my_socket.send("\nSending a list of pharmacies".encode(FORMAT))
            for pharmacy in pharmacies:
                my_socket.send(pharmacy.encode(FORMAT))
        elif choice == "done":
            my_socket.send("\nExiting".encode(FORMAT))
            my_socket.close()
    elif LoginSuccess == False:
        my_socket.send("\n invalid username or password\nExiting...".encode(FORMAT))
        my_socket.close()

def main():
    #Create a socket object
    my_socket = socket.socket()
    #Get the hostname
    host = socket.gethostname()
    #Reserve a port for your service
    port = 9999
    #Bind to the port
    my_socket.bind((host, port))
    #Wait for client connection
    my_socket.listen(5)
    while True:
        #Establish connection with client
        c, addr = my_socket.accept()
        #Start a new thread and return its identifier
        t = threading.Thread(target=client_request, args=(c, addr))
        #Start new thread
        t.start()

if __name__ == "__main__":
    main()
