from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.nepalstock.com/company/display/697')




time.sleep(2)
driver.close()
