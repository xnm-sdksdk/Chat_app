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

# listen for our incoming connection, as a param (1) because we only want one connection to be established
sckt.listen(1)




