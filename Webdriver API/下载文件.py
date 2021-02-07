"""
webdriver 允许我们设置默认的文件下载路径
"""
import os
from selenium import webdriver

fp = webdriver.FirefoxProfile()

# 0表示文件会下载到浏览器默认的下载路径 2表示下载到指定目录
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", os.getcwd())
#指定文件下载格式 "binary/octet-stream" 表示二进制文件
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()