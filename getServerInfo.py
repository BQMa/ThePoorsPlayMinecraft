#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import socket

def getinfo():
    s=socket.socket()
    iport=("cattau.dynv6.net",25565)
    s.connect(iport)
    print("connected to %s"%(str(iport)))
    msg1=bytes.fromhex("1700e003106361747461752e64796e76362e6e657463dd010100") #length=24+2
    c1=s.send(msg1) 
    print("sent: %s %d/%d"%(msg1,c1,len(msg1)))
    reply=s.recv(1500)
    print("get reply: %s"%(reply)) #b'\x90\x01\x00\x8d\x01{"description":....
    msg2=bytes.fromhex("0901000000000089586a") #length=10
    c2=s.send(msg2) 
    print("sent: %s %d/%d"%(msg2,c2,len(msg2)))
    s.close()
    print("closed socket")
    info=reply[5:len(reply)].decode("utf-8")
    print("got info: %s"%(info))

if __name__=="__main__":
    getinfo()
