from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

'''Get local session of firefox'''
browser = webdriver.Firefox()

'''Load page :  yahoo'''
browser.get("http://www.yahoo.com")

'''error check'''
assert "Yahoo" in browser.title

'''interacting with the page'''

'''find query box'''
elem = browser.find_element_by_name("p")

'''mimic keystroke interaction with page :input query string and hit return'''
elem.send_keys("seleniumhq" + Keys.RETURN)



'''Let the page load, will be added to the API'''
time.sleep(0.2)



'''error catching'''
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()

