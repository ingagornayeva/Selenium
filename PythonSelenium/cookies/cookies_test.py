#сбор куки с поиощью модуля pickle
import time
import pickle #модуль
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://vgtimes.ru/')
time.sleep(10)
pickle.dump(browser.get_cookies(), open("/Users/macbook/Documents/selenium_test/cookies/cat", "wb"))
browser.refresh()
