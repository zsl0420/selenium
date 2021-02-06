
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#参数数字为像素
print("设置浏览器窗口的大小为length:480,height:800")
"""
设置浏览器窗口大小的方法为set_window_size()
"""
driver.set_window_size(480, 800)
driver.quit()