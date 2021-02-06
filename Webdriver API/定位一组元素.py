"""
定位一组元素与定位一个元素的区别在于element 后面是否有s
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 定位一组元素
texts = driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")

#计算匹配结果个数
print(len(texts))

#循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()