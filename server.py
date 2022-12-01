# used to send messages across the network they provide a form of inter process communication (IPC - mechanisms that an OS provides ti allow the processes to manage shared data)
import socket
# imports module of system
import sys
# imports time and date
import time


# SOCKET API CALLS AND DATA FLOW FOR TCP
"""
Server:
socket
bind
listen
accept
recv
send
recv
close

Client:
socket
connect
send
recv
close
"""

# 
sckt = socket.socket()

# gets the local host name of the device
host = socket.gethostname()
# print(host) prints the name of my machine
print("Serve will start on host: ", host)

# makes the connection between devices; 8080 http alternative TCP UDP protocol 
port = 8080


# tuple
sckt.bind((host,port))

print("")

print("Server done binding to host and port successfully")

print("")

print("Server is waiting for incoming connection.")
print("")
# listen for our incoming connection, as a param (1) because we only want one connection to be established
sckt.listen(1)


# variables for connection and adress
# the var connection is assigned to the socket itself, wich is the physical circuit coming from the client
# var adress is assigned to the IP adress of the client
connection, address = sckt.accept()



print(address, "Has connected to the server and is now online.")
print("")

# loop to send comms
while 1:
    # 
    message = str(input(">>"))

    # convert the message into bytes, the interface of sockets can only support bytes
    message = message.encode()

    # establish connection with client
    connection.send(message)

    print("Message has bem sent...")
    print("")
    
    # accept message and display it
    incoming_message= sckt.recv(1024)

    # decode message
    incoming_message = incoming_message.decode()

    print("Client: ", incoming_message)
    print("")









