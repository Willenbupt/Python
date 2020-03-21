#coding=utf-8
import _thread
import time
import os
from subprocess import Popen,PIPE

def Ping(ip):
    #linux 下Ping = Popen(['/bin/bash','-c','ping -c 2'+ip],stdin=PIPE,stdout=PIPE)
    #Windows
    Ping = Popen('ping '+ip,stdin=PIPE,stdout=PIPE)
    data = Ping.stdout.read()#返回的数据类型是byte
    datas = data.decode('gb2312')#byte转string
    #if 'ttl' in data:
    if 'TTL' in datas:#windows是大写,如果有TTL这个字符串则代表成功
        print('%s is up'%ip,time.ctime())

def main():
    for i in range(1,255):
        ip = '113.107.238.'+ str(i)
        _thread.start_new_thread(Ping,(ip,))#缺点是不容易控制线程数
        #Ping(ip)
        time.sleep(0.1)

if __name__ == '__main__':
    main()

##############测试用#############
# ip='127.0.0.1'
# Ping = Popen('ping '+ip,stdin=PIPE,stdout=PIPE)
# data = Ping.stdout.read()
# datas=data.decode("gb2312")
# print(datas)
# if 'TTL' in datas:
#
#     print("ip is up")
#
