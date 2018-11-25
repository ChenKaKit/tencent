# -*- coding:utf-8 -*-
# -*-- python 3.6 --*-

import os
import re


def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            if f1.startswith('.'):
                print('要删文件: %s' % tmp_path)
                os.remove(tmp_path)
        else:
            print('文件夹：%s' % tmp_path)
            traverse(tmp_path)

# os.remove(file)


if __name__ == '__main__':
    path = 'C:\下载\爬虫课件和代码'
    traverse(path)


