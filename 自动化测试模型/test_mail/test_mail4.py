"""
通过读取text文档中的数据 read():读取整个文件 read_line():读取一行数据  read_lines():读取所有行数据
with(open("./test_mail/user_info.txt", "r")) as user_file:
    data = user_file.readlines()
"""
from selenium import webdriver
from time import sleep
from module import Mail
# 处理text文档中的数据
with (open("../data_file/user_info.txt", "r")) as user_file:
    data = user_file.readlines()

# 格式化处理
    users = []
    for line in data:
        user = line[:-1].split(":")
        users.append(user)

#打印user二维数组
    print(users)

driver = webdriver.Firefox()
driver.get("https://mail.163.com")
sleep(2)

mail = Mail(driver)

# 用户名为空
mail.login2(users[0][0], users[0][1])
