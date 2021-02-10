from time import sleep
from selenium import webdriver
from module import Mail

driver = webdriver.Firefox()
driver.get("https://mail.163.com")

mail = Mail(driver)
mail.login()
sleep(5)
driver.quit()
