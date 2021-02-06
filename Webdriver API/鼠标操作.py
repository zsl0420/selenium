"""
webdriver 中与鼠标相关的操作都封装在了ActionChains 类中
ActionChains 类提供了鼠标操作时的常用方法：
1 perform():执行ActionChains类中存储的所有行为
2 context_click(): 右击
3 double_click(): 双击
4 drag_and_drop()： 拖动
5 move_to_element(): 鼠标悬停
"""
from selenium import webdriver
#引入ActionChains 类
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# 定位到要悬停的元素》设置
above = driver.find_element_by_id("s-usersetting-top")
# 对定位元素执行鼠标悬停动作
ActionChains(driver).move_to_element(above).perform()

driver.find_element_by_link_text("搜索设置").click()

driver.quit()