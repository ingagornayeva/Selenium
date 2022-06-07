#в данном примере показано, как можно автоматизировать заполнение форм

from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/login')
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[1]/div/input').send_keys('tomsmith')
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div/input').send_keys('SuperSecretPassword!')

driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button/i').click()
time.sleep(10)
driver.quit()

