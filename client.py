# used to send messages across the network they provide a form of inter process communication (IPC - mechanisms that an OS provides ti allow the processes to manage shared data)
import socket
# imports module of system
import sys
# imports time and date
import time

sckt = socket.socket()

host = input("Enter host name of the server: ")
port = 8080


sckt.connect((host, port))

print("Connected to chat server")

# loop to listen comms
while 1:
    
    # accept message and display it
    incoming_message= sckt.recv(1024)

    # decode message
    incoming_message = incoming_message.decode()

    print("Server: ", incoming_message)
    print("")
    
    message = str(input(">>"))

    # convert the message into bytes, the interface of sockets can only support bytes
    message = message.encode()

    # establish connection with client
    connection.send(message)

    print("Message has bem sent...")
    print("")





