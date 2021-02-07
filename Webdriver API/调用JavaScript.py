"""
使用场景：
某些页面无法用webdriver 提供的API完成，比如浏览器滚动的拖条，这个时候就需要借助JavaScript来进行实现
滚动条代码：
<!-- window.scrollTo(左边距，上边距); -->
window.scrollTo(0,450)
通过使用execute_script()来执行JS代码
document.body.scrollHeight:滚动到底部
document.body.scrollTop:滚动到顶部
"""
# 例
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.set_window_size(800, 600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
# 加上等待时间 否则页面没有加载完全的话无法实现滚动
sleep(2)
# 通过JavaScript 来实现浏览器滚动条
js = "window.scrollTo(100,document.body.scrollHeight);"
driver.execute_script(js)

driver.quit()
