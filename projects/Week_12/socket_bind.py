import socket, sys

#This will bind a port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = ("localhost", 4444)
sock.bind(svr_addr)
sock.listen(1)
