import socket, sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = ("localhost", 4444)
sock.connect(svr_addr)

try:
    msg = f"Polly want a cracker?"
    sock.sendall(msg)
    data = sock.recv(4444)
    print(data)
finally:
    sock.close()
