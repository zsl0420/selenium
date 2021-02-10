"""
应用场景：当所需要的数据是不规则的，需要用一个配置文件来配置当前
平台的各种信息，一般使用xml文件来存放
"""
from xml.dom.minidom import parse

# 打开xml文件
dom = parse('../data_file/config.xml')

# 得到文档元素对象
root = dom.documentElement

#获取一组标签
tag_name = root.getElementsByTagName('*')

print(tag_name[0].firstChild.data)
print(tag_name[1].firstChild.data)
print(tag_name[2].firstChild.data)