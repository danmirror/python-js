# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys  
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err) )
# default port for socket 
port = 8124
# while(1):
try: 
    host_ip = socket.gethostbyname('192.168.43.78') 
except socket.gaierror: 
  
    # this means could not resolve the host 
    print ("there was an error resolving the host")
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 

data = "11,4,39,390"
s.send(data.encode('utf-8'))
msg = s.recv(1024)
print(msg)
s.close()
