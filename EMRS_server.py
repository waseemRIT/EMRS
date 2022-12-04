import socket
import threading

# DEFINING CONSTANTS
USER = "admin"
PASSWD = "password"
FORMAT = "utf-8"
LoginSuccess = False

# Medical Records
patients = ["Hamza : Headaches", "Mustafa : Diabetes", "Omar : Cholera", "Osama : Chickenpox", "Khalid : eczema"]
# Doctors
doctors = ["Dr. Waseem : Cardiologists", "Dr. Kassem : Anesthesiologists", "Dr. Muneer : Dermatologists", "Dr. Muaz : Endocrinologists", "Dr. Huda : Dentist"]
# Hospitals
Nurses = ["Florence Nightingale : Certified Nursing Assistant (CNA) ", "Clara Barton : Registered Nurse (RN) ", "Mary Breckinridge : Surgical Assistant Registered Nurse ", "Dorothea Dix : Emergency Room Registered Nurse ", "Margaret Sanger : Licensed Vocational Nurse (LVN)"]
# Pharmacies
equipment = ["Defibrillators", "Patient Monitors", "Sterilizers", "Surgical Tables", "Blanket and Fluid Warmers."]


def client_request(my_socket, addr):
    # Print the address of the client that just connected
    print("Connection from: " + str(addr))
    # Receive the username input from the client
    username = my_socket.recv(1024).decode(FORMAT)
    # Receive the password from the client
    password = my_socket.recv(1024).decode(FORMAT)
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
        my_socket.send("\n\nWelcome to the Dubai Palm Jumeirah CSEC Hospital\n".encode(FORMAT))
        while True:
            # Send a menu to the client
            # send a option to send Medical Records
            my_socket.send("\n[1] Send Patients Records".encode(FORMAT))
            # Send a option to send a list of doctors
            my_socket.send("\n[2] Send a list of Doctors Records".encode(FORMAT))
            # Send a option to send a list of hospitals
            my_socket.send("\n[3] Send a list of Nurses Records".encode(FORMAT))
            # Send a option to send a list of pharmacies
            my_socket.send("\n[4] Send a list of hospital equipment".encode(FORMAT))
            # type done to exit
            my_socket.send("\nType 'done' to exit\n".encode(FORMAT))
            # Receive the choices from the client
            my_socket.send("\nEnter your Choice: ".encode(FORMAT))
            choice = my_socket.recv(1024).decode(FORMAT)
            # Send the appropriate data to the client
            if choice == "1":
                my_socket.send("\nSending Patients Records".encode(FORMAT))
                for record in patients:
                    # Format the send
                    my_socket.send("\n{}".format(record).encode(FORMAT))
                    continue
            elif choice == "2":
                my_socket.send("\nSending a list of Doctors Records".encode(FORMAT))
                for doctor in doctors:
                    # Format the send
                    my_socket.send("\n{}".format(doctor).encode(FORMAT))
                    continue
            elif choice == "3":
                my_socket.send("\nSending a list of Nurses Records".encode(FORMAT))
                for nurse in Nurses:
                    # Format the send
                    my_socket.send("\n{}".format(nurse).encode(FORMAT))
                    continue
            elif choice == "4":
                my_socket.send("\nSending a list of Hospital Equipment Records".encode(FORMAT))
                for pharmacy in equipment:
                    # Format the send
                    my_socket.send("\n{}".format(pharmacy).encode(FORMAT))
                    continue
            elif choice == "done":
                my_socket.send("\nExiting".encode(FORMAT))
                print("Client disconnected " + str(addr))
                my_socket.close()
                break
    elif not LoginSuccess:
        my_socket.send("\n invalid username or password\nExiting...".encode(FORMAT))
        # Terminate the connection with the client
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
        # Start a new thread and return its identifier
        t = threading.Thread(target=client_request, args=(c, addr))
        # Start new thread
        t.start()


if __name__ == "__main__":
    main()
