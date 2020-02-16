'''
目的：实现将目录下的文件的 后缀 批量重命名
step 1 : 获取 指定目录下的 文件名  os.listdir
step 2 : 分离文件名和后缀名   os.path.splitext
step 3 : 修改后缀名          os.rename
'''
#方法一
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
'''

#改进的方法二 
'''
目的：实现将目录下的文件的 后缀 批量重命名
step 1 : 获取 指定目录下的 文件名  os.listdir
step 2 : 分离文件名和后缀名   os.path.splitext
step 3 : 修改后缀名          os.rename
'''

import os
import argparse
import sys


def suffix_rename(work_dir, old_suffix, new_suffix):
    #work_dir = "C:\\Users\\12390\\Documents\\Python\\test"
    #old_suffix = ".py"
    #new_suffix = ".java"
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        suffix = split_file[1]
        print(suffix)
        if old_suffix == suffix:
            newfile = split_file[0] + new_suffix
            print(newfile)
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))
    print("已全部修改完毕")
    print(os.listdir(work_dir))

def get_parse():
    #创建解析器
    parser = argparse.ArgumentParser(description="更改工作目录中文件的扩展名")
    #添加参数
    # metavar - 在使用方法消息中使用的参数值示例。
    # nargs - 命令行参数应当消耗的数目

    parser.add_argument('work_dir', metavar = 'WORK_DIR', type = str, nargs = 1)
    parser.add_argument('old_suffix', metavar = 'OLD_SUFFIX', type = str, nargs = 1, help = 'old_suffix')
    parser.add_argument('new_suffix', metavar = 'NEW_SUFFiX', type = str, nargs = 1, help = 'new_suffix')
    return parser

def main():

    parser = get_parse()



    # args = parse.parse_args(), 是将add_argument的所有属性给予args
    # 那么parser中增加的属性内容都会在args实例中
    # parse_args()是将之前add_argument()定义的参数进行赋值，并返回的是namespace。
    # namespace 里面存储的是 属性及其属性的值，值以list的形式存储
    # argss = parser.parse_args()
    # Namespace(new_ext=['py'], old_ext=['java'], work_dir=['C:\\Users\\12390\\Documents\\Python\\test'])
    # <class 'list'>: ['py']
    # <class 'list'>: ['java']
    # <class 'list'>: ['java']

    #var会把返回的属性和其属性的值以 字典 的形式搭配在一起
    # <class 'dict'>: {'work_dir': ['C:\\Users\\12390\\Documents\\Python\\test'], 'old_ext': ['java'], 'new_ext': ['py']}
    # vars() 函数返回对象object的属性和属性值的字典对象，把命名空间里的属性和其值转换成字典对象
    # <class 'list'>: ['C:\\Users\\12390\\Documents\\Python\\test']
    # <class 'list'>: ['java']
    # <class 'list'>: ['py']

    args = vars(parser.parse_args())
    #获取字典里'work_dir'对应的键值，因为对应的键值存储形式是list,所以有必要再获取list里的第0个元素赋予变量work_dir
    #一下其他变量同理
    work_dir = args['work_dir'][0]
    old_suffix = args['old_suffix'][0]
    if old_suffix[0] != '.':
        old_suffix = '.' + old_suffix
    new_suffix = args['new_suffix'][0]
    if new_suffix[0] != '.':
        new_suffix = '.' + new_suffix

    suffix_rename(work_dir, old_suffix, new_suffix)

if __name__ == '__main__':
    main()








