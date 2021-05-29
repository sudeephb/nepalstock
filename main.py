from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)

SEARCH_SYMBOL = 'NIFRA'

driver.get('http://www.nepalstock.com/')

stock_symbol_input = driver.find_element_by_xpath("//div[@id='search']//input[@id='stock_symbol']")
stock_symbol_input.send_keys(SEARCH_SYMBOL)

search_symbol = driver.find_element_by_xpath("//div[@id='search']//button[@id='search_symbol']")
search_symbol.click()

exec(SEARCH_SYMBOL+"_url = driver.current_url")
print('Current URL: ')
print(eval(SEARCH_SYMBOL+'_url'))

time.sleep(3)
driver.close()

