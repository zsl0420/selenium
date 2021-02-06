"""
有时候需要手动模拟浏览器F5的刷新动作
方法：driver.refresh()
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.refresh()

driver.quit()