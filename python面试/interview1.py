

#1、利用sum()函数求和
#sum(iterable[, start]) iterable是迭代对象(列表，元组，集合) start指定相加的参数，默认为0
#range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表
#list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表
sum(range(1,101))


#2、在函数内部修改全局变量
#利用globle在函数声明

a = 5
def fn():
    global a
    a = 4

fn()
print(a)

#3、五个python标准库
import os
import sys
import re
import math
import datetime

#4、字典如何删除和合并两个字典
dic = {"name":"zs","age":18}
del dic["name"]

dic2 = {"name":"ls"}
dic.update(dic2)

#5、谈下python的GIL： GIL是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序时候会霸占python解释器
#使得进程内其他线程无法运行，等该线程运行完成后其他线程才能运行，需要该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，解锁器会打开，是其他线程运行
#所以多线程中，运行是有先后顺序的，不是同时进行
#多进程中因为每个进程都可以被系统分配资源，相当于每个进程都有一个python解释器，所以进程可以同时进行，但是开销大

#6、python实现列表去重的方法

#先通过集合去重，再转列表
#列表解析是Python迭代机制的一种应用，它常用于实现创建新的列表，因此用在[]中。
#[expression for iter_val in iterable]

lis = [1,1,2,2,3,3,4,4]
a = set(lis)
# 先编译for x in a 遍历一遍集合，再赋值给左边的表达式
[x for x in a]

#7、fun(*arg,**kwargs)中的*arg,**kargs的意思
#*arg 和 **kargs 用于函数定义，可以将不定数量的参数传递给一个函数，一开始可能不会知道会传递多少个参数
#*arg用来发送一个非键值对的可变数量的参数列表给函数
def demo(args_f,*args_v):
    print('args_f = '+ args_f)
    for x in args_v:
        print('args_v = '+ x)
demo('a','b','c','d')
# args_f = {str}'a'
# args_v={tuple} <class 'tuple'>: ('b', 'c', 'd')

#**kargs允许不定长度的键值对，作为参数传递给一个函数。如果想要在一个函数里处理带名字的参数
def demo1(**args_v):
    for k,v in args_v.items():
        print(k,v)
demo1(name = 'njcx')

#8、python2 和 python 3的range(100)的区别
#python2 返回列表，python3返回迭代器

#9、什么样的语言可以用装饰器
#函数可以作为参数传递的语言，能够使用装饰器

#10、python内建的数据类型: int、bool、str、list、tuple、dict
































