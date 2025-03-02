#编写第一个自动化脚本文件

from selenium import webdriver

driver = webdriver.Firefox()
"""
    用的是火狐浏览器
"""
driver.get("https://www.baidu.com")
sleep(2)

# 定位元素
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

#退出浏览器
driver.quit()
