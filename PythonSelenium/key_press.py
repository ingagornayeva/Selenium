#в данном примере показаны возможности имитации нажатия клавиш на клавиатуре

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/key_presses')

driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input').send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input').send_keys(Keys.DELETE)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input').send_keys(Keys.TAB)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input').send_keys(Keys.SHIFT)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input').send_keys(Keys.ESCAPE)
time.sleep(1)


driver.quit()








