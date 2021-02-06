"""
页面操作过程中，可能某些链接会打开新的页面，这个时候就需要切换到新的窗口进行操作
webdriver 提供的方法switch_to.window()可以实现
current_window_handle:获取到当前窗口句柄
window_handles:返回所有窗口的句柄到当前会话
switch_to.window():切换到相应的窗口
"""
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获取到百度搜索窗口句柄
currentWin = driver.current_window_handle

driver.find_element_by_link_text("学术").click()
time.sleep(1)

# 获取当前所有窗口的句柄
all_handles = driver.window_handles


# 进入学术窗口
for handle in all_handles:
    if currentWin == handle:
        continue
    else:
        driver.switch_to.window(handle)
        time.sleep(10)
        print(driver.title)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)

# 关闭当前窗口
driver.close()
# 回到百度首页
driver.switch_to.window(currentWin)
print(driver.title)

driver.quit()