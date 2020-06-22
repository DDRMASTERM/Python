import socket, sys
# Create socket instance
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#The server will listen for oncoming connections
while True:
	connection, client_addr = sock.accept()
	try:
		while True:
			data = connection.recv(4444)
			if data:
				connection.sendall(data)
			else:
				break
	finally:
		connection.close()

