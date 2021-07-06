#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2021/7/6 18:01
# @Author   : dapwn
# @File     : read_file.py
# @Software : PyCharm
def read_file(file_path):
    BLOCK_SIZE = 1024
    with open(file_path, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


if __name__ == '__main__':
    file_path = '../data/test.txt'
    for _ in read_file(file_path=file_path):
        print(_)
    # result = read_file(file_path=file_path)
    # print(result)
