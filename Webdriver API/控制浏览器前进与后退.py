"""
控制浏览器前进与后退方法
后退:driver.back()
前进:driver.forward()
"""
from selenium import webdriver

driver = webdriver.Firefox()

#访问百度首页
first_url = 'https://www.baidu.com'
print("now access %s" % (first_url))
driver.get(first_url)

#访问新闻首页
senceond_url = 'https://news.baidu.com'
print("now access %s" % (senceond_url))
driver.get(senceond_url)

# 返回（后退）到百度首页
print("back to %s" % (first_url))
driver.back()

# 前进到新闻页
print("forward to %s" % (senceond_url))
driver.forward()

driver.quit()