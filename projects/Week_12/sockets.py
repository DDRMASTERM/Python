import socket, sys
# Create socket instance
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Website to connect to
web_server = ("www.google.com", 80)

# sock connect
sock.connect(web_server)

# sock close
sock.close()

