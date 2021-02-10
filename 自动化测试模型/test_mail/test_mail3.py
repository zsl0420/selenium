from selenium import webdriver
from time import sleep
from module import Mail

driver = webdriver.Firefox()
driver.get("https://mail.163.com")
sleep(2)

mail = Mail(driver)
# 测试用例集
# 用户名密码为空
mail.login2(" ", " ")
#用户名为空
mail.login2("", "zsl*******")
#密码为空
mail.login2("zsl*******", "")
#用户名密码错误
mail.login2("zsl******", "fjsdlkfjlsa")
