step1 : 获取并打印出当前用户目录  os.path.expanduser
step2 ：输入目录名判断是否有相同目录  os.path.exists  os.path.join(home, TESTDIR)
step3 ：没有则创建该目录        os.makedirs
step4 ：否则则打印已存在

'''

'''
import os

Message = "这个文件已经存在"

UserPath = os.path.expanduser('~')
makedir = input()
if not os.path.exists(os.path.join(UserPath,makedir)):
    os.mkdir(os.path.join(UserPath,makedir))
else:
    print(Message)
'''

'''
目的：在用户目录创建不存在的文件夹
step1 : 获取并打印出当前用户目录  os.path.expanduser
step2 ：输入目录名判断是否有相同目录  os.path.exists  os.path.join(home, TESTDIR)
step3 ：没有则创建该目录        os.makedirs
step4 ：否则则打印已存在

'''

import os
import argparse
import sys

Message = "这个文件已经存在"

def create_dir(makedir):
    UserPath = os.path.expanduser('~')
    if not os.path.exists(os.path.join(UserPath,makedir)):
        os.mkdir(os.path.join(UserPath,makedir))
        print('成功创建%s文件夹',makedir)
    else:
        print(Message)

def get_parser():
    parser = argparse.ArgumentParser(description="在用户目录创建新目录")
    parser.add_argument('makedir', metavar = 'MAKEDIR', nargs = 1, type = str)
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    makedir = args['makedir'][0]

    create_dir(makedir)

if __name__ == '__main__':
    main()



