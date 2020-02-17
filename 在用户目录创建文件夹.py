step1 : 获取并打印出当前用户目录  os.path.expanduser
step2 ：输入目录名判断是否有相同目录  os.path.exists  os.path.join(home, TESTDIR)
step3 ：没有则创建该目录        os.makedirs
step4 ：否则则打印已存在

'''

import os

Message = "这个文件已经存在"

UserPath = os.path.expanduser('~')
makedir = input()
if not os.path.exists(os.path.join(UserPath,makedir)):
    os.mkdir(os.path.join(UserPath,makedir))
else:
    print(Message)
