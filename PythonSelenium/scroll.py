from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/infinite_scroll')

element = driver.find_element_by_tag_name('html')

for i in range(500):
    driver.find_element_by_tag_name('html').send_keys(Keys.END)
    
#имитирован бесконечеый скроллинг нажатием кнопки END