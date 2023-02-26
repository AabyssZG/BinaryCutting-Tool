#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import argparse
import string
import binascii
import os, sys
from filesplit.split import Split
from filesplit.merge import Merge

def title():
    logo = r'''
 ▄▄▄▄    ██▓ ███▄    █  ▄▄▄       ██▀███ ▓██   ██▓ ▄████▄   █    ██ ▄▄▄█████▓▄▄▄█████▓ ██▓ ███▄    █   ▄████ 
▓█████▄ ▓██▒ ██ ▀█   █ ▒████▄    ▓██ ▒ ██▒▒██  ██▒▒██▀ ▀█   ██  ▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██▒▓██  ▀█ ██▒▒██  ▀█▄  ▓██ ░▄█ ▒ ▒██ ██░▒▓█    ▄ ▓██  ▒██░▒ ▓██░ ▒░▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▀▀█▄   ░ ▐██▓░▒▓▓▄ ▄██▒▓▓█  ░██░░ ▓██▓ ░ ░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓░██░▒██░   ▓██░ ▓█   ▓██▒░██▓ ▒██▒ ░ ██▒▓░▒ ▓███▀ ░▒▒█████▓   ▒██▒ ░   ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ██▒▒▒ ░ ░▒ ▒  ░░▒▓▒ ▒ ▒   ▒ ░░     ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░  ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░▓██ ░▒░   ░  ▒   ░░▒░ ░ ░     ░        ░     ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░  ▒ ░   ░   ░ ░   ░   ▒     ░░   ░ ▒ ▒ ░░  ░         ░░░ ░ ░   ░        ░       ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░       ░           ░       ░  ░   ░     ░ ░     ░ ░         ░                        ░           ░       ░ 
      ░                                   ░ ░     ░                                                          
                                  [+] BinaryCutting-Tool V1.0                                         
                                    [+] 二进制文件切割&合并工具                             
                                      [+] Author: 曾哥(@AabyssZG)              
                                        [+] Whoami: https://github.com/AabyssZG  
                                                   
'''
    print(logo)

def FileRead(filename):
    try:
    	f =open(filename)                               #打开目标文件
    	f.close()
    except FileNotFoundError:
    	print ("未找到同目录下的二进制文件" + filename) #如果未找到文件，输出错误
    	return                                         #退出线程，进行详细报错
    except PermissionError:
    	print ("无法读取目标文件（无权限访问）")     #如果发现目标文件无权限，输出错误
    	return                                         #退出线程，进行详细报错
    
def Cutting(filename, filesize):
    if os.path.exists("./output"):
    	print(f"切割文件夹已经存在，无需创建")
    	datanames = os.listdir("./output")
    	for i in datanames:
    		c_path = os.path.join("./output", i)
    		if os.path.isdir(c_path):#如果是文件夹那么递归调用一下
    			del_file(c_path)
    		else:                    #如果是一个文件那么直接删除
    			os.remove(c_path)
    	print(f"[+] 已经清空切割文件夹./output")
    else:
    	os.mkdir("./output")
    	print(f"切割文件夹不存在，已经创建")
    print('\n')
    file_url = "./" + filename
    print(f"切割文件大小为{filesize}KB")
    print(f"[+] 正在读取指定文件:{file_url}")
    split = Split(file_url, "./output")
    print(f"[+] 正在切割指定文件:{file_url} 到./output目录")
    filesize = 1024*filesize
    split.bysize(filesize)
    print('切割二进制文件结束，导出结果位于/output目录')

def Merger(filename):
    if os.path.exists("./merge"):
    	print(f"合并文件夹已经存在，无需创建")
    else:
    	os.mkdir("./merge")
    	print(f"合并文件夹不存在，已经创建")
    print('[+] 正在读取/output文件夹下的内容')
    datanames = os.listdir("./output")
    list = []
    for i in datanames:
    	list.append(i)
    print(list)
    merge = Merge(inputdir = "./output", outputdir="./merge", outputfilename = filename)
    print('\n')
    print('[+] 成功读取，对文件进行合并中')
    merge.merge()
    print(f"合并成功，导出结果位于/merge目录，合并文件名为{filename}")

if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser(description="BinaryCutting-Tool V1.0", epilog='二进制文件切割&合并工具')
    parser.add_argument('-c', action='store', dest='cutting', type=str, help='切割目标二进制文件并导出')
    parser.add_argument('-m', action='store', dest='merger', type=str, help='合并切割后的文件并导出')
    parser.add_argument('-s', action='store', dest='size', type=int, default='1024', help='设定切割文件的大小，默认1024KB')
    args = parser.parse_args()
    try:
        if args.cutting:
        	  FileRead(args.cutting)
        	  Cutting(args.cutting, args.size)
        if args.merger:
        	  Merger(args.merger)
    except BaseException as e:
        err = str(e)
        print('脚本详细报错：' + err)
