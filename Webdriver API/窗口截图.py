"""
使用场景：在自动化测试中可以用来截图报错等信息
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 截取当前网页截图，指定保存位置
driver.save_screenshot("./image/baidu_img.png")

driver.quit()