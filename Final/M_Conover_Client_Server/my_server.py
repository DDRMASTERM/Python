# Matthew Conover
# IS 3750
# Server

import socket, sys, optparse

# Set up optparse
parser = optparse.OptionParser()

# Server setup option
parser.add_option("-s", "--server", default = "localhost", 
dest="server", help="The server you want to connect to", metavar = "SERVER")

# Port setup option
parser.add_option("-p", "--port", default = 4444, 
dest="port", help="The port you intend to use", metavar = "PORT")
	
# Parse the options
(options, args) = parser.parse_args()

# The server listens for incoming connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = (options.server, int(options.port))
sock.bind(svr_addr)

# Store the server's IP address
ipA = socket.gethostbyname(svr_addr[0])

# The server prints a message stating the listening address and port 
print(f"{svr_addr[0]} at {ipA} is listening on port {svr_addr[1]}")
sock.listen(1)


# The server will listen for oncoming connections
while True:
	
	# Accept incoming connection
	connection, client_addr = sock.accept()
	
	#The server prints a message stating the address of the client
	print(f"Connection from {client_addr}")
	try:
		while True:
			# Data is received from connection
			data = connection.recv(1024)
			
			# Data was received
			if data:
				# Decode message
				message = data.decode("utf8")
				message = message.title()
				# Create and return a message
				data = f"Hello {message}!"
				
				# Encode then send message
				msg = data.encode("utf8")
				connection.sendall(msg)
				
			# No data was received
			else:
				# End loop
				break
	finally:
		
		# Close the connection
		connection.close()
