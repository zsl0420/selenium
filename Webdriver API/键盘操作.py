"""
模拟常用键盘操作
"""
from selenium import webdriver
#调用Keys模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 定位输入框方法
input = driver.find_element_by_id("kw")

# 输入框中输入内容
input.send_keys("seleniumm")

#删除多输入的一个m
input.send_keys(Keys.BACK_SPACE)

# 输入空格键 + “教程”
input.send_keys(Keys.SPACE)
input.send_keys("教程")

#输入组合键CTRL + a，全选输入框内容
input.send_keys(Keys.CONTROL, 'a')

# 输入组合键CTRl + x，剪切输入框内容
input.send_keys(Keys.CONTROL, 'x')

# 输入组合键CTRL+v, 粘贴内容到输入框
input.send_keys(Keys.CONTROL, 'v')

#用回车键代替单击操作
input.send_keys(Keys.ENTER)

driver.quit()
