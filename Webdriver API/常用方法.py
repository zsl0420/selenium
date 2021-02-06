"""
定位到元素之后，需要对元素进行各种各样的模拟操作
webdriver 中常用的方法有
1 clear():用于输入框中的文本信息
2 send_keys(value):用于向文本框中输入文字
3 click():单击元素操作
4 submit(): 提交表单 用于某些搜索框不提供搜索按钮，通过键盘的enter键完成
    可以与clcik()互换使用
5 size:返回元素的尺寸
6 text:获取元素的文本
7 get_attribute(name): 获得属性值
8 is_displayed(): 设置元素是否用户可见
"""
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").clear()

size = driver.find_element_by_id("su").size
print(size)

#返回百度页面底部备案信息
text = driver.find_element_by_id("bottom_layer").text
print(text)

# 返回元素的属性值，可以是id/name/type 或者其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

#返回元素的结果是否可见，返回结果为true 或者 为false
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

driver.quit()