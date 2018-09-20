#!/usr/bin/python
# -*- coding: utf-8 -*-
import shutil
from os import listdir
from os.path import isfile, isdir, join
from os import walk


# 取得所有檔案與子目錄名稱
def print_fIle(path):
    files = listdir(path)

    # 以迴圈處理
    for f in files:
        # 產生檔案的絕對路徑
        fullpath = join(path, f)
        # 判斷 fullpath 是檔案還是目錄
        if isfile(fullpath):
            print("檔案：", fullpath)
        elif isdir(fullpath):
            # print("目錄：", fullpath)
            print_fIle(fullpath)


def print_fIle2(path):
    # 遞迴列出所有檔案的絕對路徑
    for root, dirs, files in walk(path):
        for f in files:
            fullpath = join(root, f)
            # print(fullpath)
            if '.url' in fullpath:
                print("rm '" + fullpath + "'")


def move_file(path):
    for root, dirs, files in walk(path):
        for f in files:
            fullpath = join(root, f)
            # print(fullpath)
            if 'MP3' in fullpath:
                # print('root===>' + root)
                new_path = root.replace('/MP3', '')
                print(new_path)
                shutil.move(fullpath, new_path)


def delete_file(path):
    for root, dirs, files in walk(path):
        for f in dirs:
            fullpath = join(root, f)
            # print(fullpath)
            if 'MP3' in dirs:
                # print('root===>' + root)
                print(fullpath)
                shutil.rmtree(fullpath)


# 指定要列出所有檔案的目錄
path = "/media/ed/TOSHIBA EXT/ACG2018"

delete_file(path)

'''
fullpath 為一字串 如果裡面有 .url print 出來
if '.url' in fullpath:
    print("rm '" + fullpath + "'")
'''
