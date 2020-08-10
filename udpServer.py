from socket import *
from time import ctime

HOST = ''
PORT = 9090
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("...waiting for message...")
    data,ADDR = udpSerSock.recvfrom(BUFSIZE)
    if data is None:
        break
    print("[%s]: From Address %s:%s receive data: %s" %(ctime(), ADDR[0], ADDR[1], data.decode('utf-8')))
    
    send_data = "FYI, I have received > " + data.decode('utf-8') + " from you."
    if send_data is not None:
        udpSerSock.sendto(send_data.encode('utf-8'), ADDR)

udpSerSock.close()