"""
创建一个module.py 文件来存放登陆动作和退出动作
"""
# 创建一个Mail类，来存放登陆退出动作
class Mail:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        """登录"""
        login_frame = self.driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("zsl******")
        self.driver.find_element_by_name("password").send_keys("zsl******")
        self.driver.find_element_by_id("dologin").click()

    def logout(self):
        self.driver.find_element_by_link_text("退出").click()

# 登录数据参数化
    def login2(self, username, password):
        login_frame = self.driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()
