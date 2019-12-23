#!/usr/bin/python3
import socket
import time
import psutil
from _thread import *
import threading
import time
import sys
import graph

ip=""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        
    return False
def Enquiry(infolist): 
    if not infolist[0]==" ": 
        return 1
    else: 
        return 0


HEADERSIZE = 10
#socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.1.100"
port=4321
s.bind((socket.gethostname(),port))
s.listen(5)

def clientthread(clientsocket):
    i = 0
    f1 = open(ip,"w")
    f1.close()
    true=True

    while true:
        full_msg = ''
        new_msg = True

        while True:
            
            msg = clientsocket.recv(50)
            string=msg.decode("utf-8")
            string=string[3:].strip()

            if string:
                infolist= string.split('-')
                if(Enquiry(infolist)):
                    if not is_number(infolist[0]):
                        infolist[0]="0"
                    if not is_number(infolist[1]):
                        infolist[1]="0"
                    if not is_number(infolist[2]):
                        infolist[2]="0"
                    print("string:"+infolist[0]+" "+infolist[1]+" "+infolist[2]+" "+infolist[3],"msg:"+msg.decode("utf-8"))
                    file="data/"+str(infolist[3])+".txt"
                    
                    f2 = open(file, "a")
                    info=str(i)+","+infolist[0]+"-"+str(i)+","+infolist[1]+"-"+str(i)+","+infolist[2]+"-"+infolist[3]+"\n"
                    f2.write(info)
                    i+=2
                    full_msg += msg.decode("utf-8")
                    print("full length:",len(full_msg))
                    f2.close()
            else:
                print("disconnected")
                clientsocket.close()
                break
        true=False


            
      
ip=""


while True:
    
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.\n")
    welcome = f"you are connected to {socket.gethostbyname(socket.gethostname())}"
    clientsocket.send(bytes(welcome,"utf-8"))
    ip="data/"+str(address[0])+".txt"
    
    start_new_thread(clientthread,(clientsocket,))
    



s.close()
    
    

    
