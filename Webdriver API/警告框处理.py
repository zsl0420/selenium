"""
Webdriver 中处理Javascript生成的alert/confir/promt
方法：用switch_to.alert()方法定位，然后用text/accept/dismiss/send_keys等进行操作
text:返回alert confirm prompt 中的文字信息
accept()：接受现有警告框
dismiss()：解散现有警告框
send_keys()：在警告框中输入文本
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

br = webdriver.Firefox()
br.get("https://www.baidu.com")

#打开搜索设置
setting = br.find_element_by_id('s-usersetting-top')
ActionChains(br).move_to_element(setting).perform()
br.find_element_by_link_text('搜索设置').click()

#保存设置
br.find_element_by_class_name('prefpanelgo').click()

#获取警告框,这里与书中不同 alert 不带括号
alert = br.switch_to.alert

#获取警告框的信息
alert_text = alert.text
print(alert_text)

#接取警告框
alert.accept()

br.quit()