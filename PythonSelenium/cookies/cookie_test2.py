import time
from selenium import webdriver
import pickle

browser = webdriver.Firefox()
browser.get('https://vgtimes.ru/') #куки сохранены только для этого сайта
time.sleep(5)

for cookie in pickle.load(open('/Users/macbook/Documents/selenium_test/cookies/cat', 'rb')):
    browser.add_cookie(cookie)
    

print('Куки загружены')
browser.refresh()

