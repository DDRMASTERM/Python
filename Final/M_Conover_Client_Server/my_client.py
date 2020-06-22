# Matthew Conover
# IS 3750
# Client

import socket, sys, optparse

# Set up optparse
parser = optparse.OptionParser()

# Server setup option
parser.add_option("-s", "--server", default = "localhost", 
dest="server", help="The server you want to connect to", metavar = "SERVER")

# Port setup option
parser.add_option("-p", "--port", default = 4444, 
dest="port", help="The port you intend to use", metavar = "PORT")

	
# Name option
parser.add_option("-n", "--name", default = "world", 
dest="name", help="Say hello to NAME", metavar = "NAME")

# Parse the options
(options, args) = parser.parse_args()

# Setup socket and server address
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_addr = (options.server, int(options.port))

# Connect to svr_addr
sock.connect(svr_addr)

# Print server connection after successful connection
print(f"Client has connected to {svr_addr[0]} at port {svr_addr[1]}")


try:
	# Store and encode name
    message = options.name
    msg = message.encode("utf8")
    sock.sendall(msg)
    
    # Return and print response
    data = sock.recv(1024)
    received = data.decode("utf8")
    print(received)
    
finally:
	
	# Close the socket
    sock.close()
