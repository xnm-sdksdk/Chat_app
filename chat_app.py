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












