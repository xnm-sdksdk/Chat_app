# used to send messages across the network they provide a form of inter process communication (IPC - mechanisms that an OS provides ti allow the processes to manage shared data)
import socket
# imports module of system
import sys
# imports time and date
import time


# gets the local host name of the device
host = socket.gethostname()
# print(host) prints the name of my machine
print("Serve will start on host: ", host)

# makes the connection between devices; 8080 http alternative TCP UDP protocol 
port = 8080




