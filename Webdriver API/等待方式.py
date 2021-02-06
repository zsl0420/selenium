"""
webdriver 提供了两种等待方式
显式等待：是WebDriver 等待某个条件成立则继续执行，否则在达到最大时间抛出超时异常(TimeoutException)
隐式等待：当脚本执行到某个元素定位时，如果元素存在，则继续执行，如果定位不到元素，则它将以轮询的方式不断的
    判断元素是否存在，直至超出预设时间，抛出异常
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import ctime
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")
# # 显式等待
# element = WebDriverWait(driver, 5, 0.5).until(
#     EC.visibility_of_element_located((By.ID, "kw"))
#     )
# element.send_keys('selenium')
# driver.quit()

# 隐式等待
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
