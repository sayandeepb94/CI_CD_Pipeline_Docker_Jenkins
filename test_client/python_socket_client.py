import socket

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect(('127.0.0.1', 5000))

msg = s.recv(1024)

print("received ::: ", msg.decode())