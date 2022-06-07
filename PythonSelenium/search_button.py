from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://b2c.by/')
driver.maximize_window()

search_box = '/html/body/div[1]/section/div[1]/div/div/div[2]/input'
driver.find_element_by_xpath(search_box).send_keys('маникюр')
time.sleep(3)

src_btn = '/html/body/div[1]/section/div[1]/div/div/div[2]/div/span/img'
driver.find_element_by_xpath(src_btn).click()

time.sleep(3)




