"""
多表单切换就是web页面中，可能会有不同的frame/iframe 表单嵌套
而webdriver 只能在一个页面中识别到元素
使用场景：无法定位到另一个表单中的元素时，需要切换到所要定位元素的表单里面
方法：switch_to.frame()
"""
# 126 邮箱登陆

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.126.com")
sleep(2)

login_frame = driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
# 元素操作结束之后记得切换回默认的表单
driver.switch_to.default_content()

driver.quit()
