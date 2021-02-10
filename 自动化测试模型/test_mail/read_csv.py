"""
通过读取csv 文件来获取数据
"""
import csv
#codes python标准的模块编码和解码七
import codecs
# islice 用于操作迭代对象的函数
from itertools import islice

#读取本地csv文件
data = csv.reader(codecs.open('../data_file/user_info2.csv', 'r', 'gbk'))

#存放用户数据
users = []

#循环输出每行信息
for line in islice(data, 1, None):
    users.append(line)

print(users)