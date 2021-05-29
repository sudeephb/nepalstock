from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)

def get_url(stock_symbol):
    SEARCH_SYMBOL = 'NIFRA'

    driver.get('http://www.nepalstock.com/')

    stock_symbol_input = driver.find_element_by_xpath("//div[@id='search']//input[@id='stock_symbol']")
    stock_symbol_input.send_keys(stock_symbol)

    search_symbol = driver.find_element_by_xpath("//div[@id='search']//button[@id='search_symbol']")
    search_symbol.click()

    exec(SEARCH_SYMBOL+"_url = driver.current_url")
    driver.close()

    return eval(SEARCH_SYMBOL+'_url')
