"""
在进行web 自动化，用的最多的就是title/current_url/text 验证信息
1 title:用于获取当前页面的标题
2 current_url:用于获取当前页面的url
3 text:用于获取当前页面的文本信息
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print('Before search=======================')

#打印当前页面的title
title1 = driver.title
print("title:" + title1)

#打印当前页面url
now_url1 = driver.current_url
print("URL:"+now_url1)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

print('After search=========================')

# 再次打印当前页面title
title2 = driver.title
print("title:"+title2)

#再次打印当前页面url
now_url2 = driver.current_url
print("URL:"+now_url2)

#获取搜索结果条数
num = driver.find_element_by_class_name('nums').text
print("result:"+num)

driver.quit()