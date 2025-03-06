import time

import numpy as np
import socket

print("this is demo python console application in docker")

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# Creating a socket server for example
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 5000))
print("Starting the socket server, listening ...")


s.listen()
client, addr = s.accept()
print("Connection from client :: ", addr)
client.send("This is a demo message from server!!".encode())
time.sleep(10)
client.close()
