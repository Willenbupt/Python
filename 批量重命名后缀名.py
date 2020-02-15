'''
目的：实现将目录下的文件的 后缀 批量重命名
step 1 : 获取 指定目录下的 文件名  os.listdir
step 2 : 分离文件名和后缀名   os.path.splitext
step 3 : 修改后缀名          os.rename
'''

import os
import argparse
import sys


def suffix_rename():
    work_dir = "C:\\Users"
    old_suffix = ".py"
    new_suffix = ".java"
    for filename in os.listdir(work_dir): #获取指定目录的文件名字列表 并一一读取列表里的文件名
        split_file = os.path.splitext(filename) #分离文件名里的前后缀名
        suffix = split_file[1]
        print(suffix)
        if old_suffix == suffix:
            newfile = split_file[0] + new_suffix
            print(newfile)
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile)) #修改后缀名
    print("已全部修改完毕")
    print(os.listdir(work_dir))

if __name__ == '__main__':
    suffix_rename()




