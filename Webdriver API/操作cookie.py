"""
使用场景：需要验证浏览器中的cookie是否正确，基于真实的cookie无法通过白盒测试和集成测试
webdriver中提供了操作Cookie的相关方法。可以读取/添加/删除cookie
主要方法如下：
1.get_cookies():获取所有cookie
2.get_cookie(name):返回字典中key为name 的cookie
3.add_cookie(cookie_dict):添加cookie
4.delete_cookie(name,OpenString):删除名为OpenString 的cookie
5.delete_all_cookies():删除所有cookie
"""
# 获取浏览器所有cookie
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#获取所有cookie信息并打印
cookie = driver.get_cookies()
print(cookie)



# 添加cookie 信息
driver.add_cookie({'name': 'key-aaaaaa','value': 'value-bbbbbb'})

#遍历指定的Cookies
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

#删除添加的cookie信息
driver.delete_cookie('key-aaaaaa')
cookie2 = driver.get_cookies()
print(cookie2)
driver.quit()