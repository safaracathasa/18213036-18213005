#Create Client

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
data = None

s.connect((host, port))
print s.recv(1024)
while (data != "client exit"):
	data = raw_input();
	s.sendall(data)
	if data == "client exit" :
		print '\n--exiting--\n'
		break
	print s.recv(1024)
s.close
