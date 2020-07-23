#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
# host = socket.gethostname()                           

port = 4444                                          

# bind to the port
serversocket.bind(('', port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   c,addr = serversocket.accept()      
   msg = c.recv(1024)

   print("Got a connection from %s" % str(addr))
   print(msg)
   msg = 'Thank you for connecting'+ "\r\n"
   c.send(msg.encode('utf-8'))
   # c.send(bytes("21"))
   c.close()