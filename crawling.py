import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/dltjr/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://eis.cbnu.ac.kr/cbnuLogin')

driver.find_element_by_name('uid').send_keys('2018037049')
driver.find_element_by_name('pswd').send_keys('!1601a0389')

driver.find_element_by_xpath('//*[@id="commonLoginBtn"]').click()

driver.get('https://eis.cbnu.ac.kr/CBNU/index.html')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#print(soup.find_all(''))


