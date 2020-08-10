from socket import *
from time import ctime

HOST = 'localhost'
PORT = 9090
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    sendData = input("> ")
    if sendData is None:
        break
    udpCliSock.sendto(sendData.encode('utf-8'),ADDR) 
    
    print("...waiting for response...")
    recv_data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if recv_data is not None:
       print("[%s]: receiving data from server %s:%s  :%s" %(ctime(),ADDR[0],ADDR[1],recv_data.decode('utf-8')))
    
udpCliSock.close()