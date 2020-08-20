import socket
import sys

# if len(sys.argv) == 3:
#     # Get "IP address of Server" and also the "port number" from
#     argument 1 and argument 2
#     ip = sys.argv[1]
#     port = int(sys.argv[2])
# else:
#     print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
#     exit(1)

port=8080
# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
s.bind(('127.0.0.1', port)) 
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######")
    data, address = s.recvfrom(4096)
    data = data.decode('utf-8')
    print("\n\n 2. Server received: ", data, "\n\n")
    # send_data = input("Type some text to send => ")
    s.sendto(data.encode('utf-8'), address)
    print("\n\n 1. Server sent : ", data,"\n\n")