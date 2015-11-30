from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

'''Get local session of firefox'''
browser = webdriver.Firefox()

'''Load page :  yahoo'''
# browser.get("http://www.yahoo.com")
browser.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

'''error check'''
# assert "Yahoo" in browser.title
# assert "o2" in browser.title

'''interacting with the page'''

'''find query box'''
# elem = browser.find_element_by_name("p")
elem = browser.find_element_by_id("countryName") # Find the query box

'''mimic keystroke interaction with page :input query string and hit return'''
# elem.send_keys("seleniumhq" + Keys.RETURN)
elem.send_keys("Canada" + Keys.RETURN)


'''click the monthly button'''
browser.find_element_by_css_selector('.btn_arrow_tab').click()


# '''retrieve the Base rate'''
# Base = browser.find_element_by_name('base')
# print "this is the Base rate"

# '''retrieve the BoltOnFave3 rate'''
# Base = browser.find_element_by_name('base')
# print "this is the BoltOnFave3 rate"

# '''retrieve the CallCard rate'''
# Base = browser.find_element_by_name('CallCard')
# print "this is the CallCard rate"

'''IDEAS'''

'''feed countries as sys parameters, move through list with list comprehension,
create as keys in default dict for export to excel or JSON format'''

'''build in error checking if required elements are not found on the search page'''

'''error for country not found'''

'''error for Base rate not found'''

'''error for BoltOnFave3 not found'''

'''error for CallCard not found'''

'''pretty print rates for each country / export to Excel spreadsheet???'''
'''Let the page load, will be added to the API'''
time.sleep(0.2)



# '''error catching'''
# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
# browser.close()

