import os
import sys
import os.path
import platform
import socket
import pandas as pd

if platform.system().lower() == 'windows':
    print("当前运行环境是 windows")
elif platform.system().lower() == 'linux':
    print("当前运行环境是 linux")


# 获取本机计算机名称
hostname = socket.gethostname()
print(hostname)
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)


os.chdir(sys.path[0])
# getcwd返回的路径不好用
print("当前路径 -> %s" % os.getcwd())

df = pd.read_csv('../data/SURF_CHN_MUL_HOR_demo.txt', sep=' ', header=0)

df1 = pd.read_excel(r'../data/空气质量.xlsx')
df1.head(2)