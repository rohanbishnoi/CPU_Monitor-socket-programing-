#!/usr/bin/python3

import socket
import time
import psutil



import time   


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
#socket.gethostname()
HEADERSIZE = 10
host="192.168.43.60"
port=4321
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

msg=s.recv(35)
msg=msg.decode("utf-8")
print(msg)

while True:


    time.sleep(1)
    msg = f"{psutil.cpu_percent()}"+"-"+f"{psutil.virtual_memory()[2]}"+"-"+f"{psutil.disk_usage('c:')[3]}"+"-"+f"{socket.gethostbyname(socket.gethostname())}"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    print(msg)

    s.send(bytes(msg,"utf-8"))
    


        
        