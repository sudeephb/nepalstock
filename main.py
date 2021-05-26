from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.nepalstock.com/company/display/697')

stock_symbol_input = driver.find_element_by_xpath("//div[@id='search']//input[@id='stock_symbol']")
stock_symbol_input.send_keys('NIFRA')


time.sleep(2)
driver.close()
