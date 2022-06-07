from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.w3schools.com/')
time.sleep(5)

driver.get_screenshot_as_file('screenshot1.png')
driver.quit()
