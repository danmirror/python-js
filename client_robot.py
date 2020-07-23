# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys  
import json 

def Convert(string): 
    li = list(string.split(",")) 
    return li 
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += str(ele) 
        str1 +=","  
    else:
        str1 = str1[:-1]
    # return string   
    return str1  
    
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err) )
# default port for socket 
port = 8124
  
try: 
    host_ip = socket.gethostbyname('127.0.0.1') 
except socket.gaierror: 
  
    # this means could not resolve the host 
    print ("there was an error resolving the host")
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 
list_s = [2,3,4]
data = listToString(list_s)
print(data)
s.send(data.encode('utf-8'))
msg = s.recv(1024)
msg= Convert(msg)
print(msg)
s.close()
