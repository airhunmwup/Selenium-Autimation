from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("driver/chromedriver.exe")

url  = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
username = 'youremail@email.com'
password = 'yourpassword,here'

driver.get(url)

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("from__button--floating").click()

#driver.find_element_by_class_name("btn__secondary--large-muted").click()

#driver.get("https://www.linkedin.com/sales/homepage")

driver.get("https://www.linkedin.com/sales/search/people?viewAllFilters=true")
time.sleep(2)
driver.find_element_by_id("ember153").click()
time.sleep(2)
driver.find_element_by_id("ember153-typeahead").send_keys("construction")
time.sleep(2)
driver.find_element_by_class_name("search-filter-typeahead__suggestion-item-value").click()
time.sleep(2)
driver.find_element_by_id("ember196").click()
time.sleep(2)
driver.find_element_by_id("ember196-typeahead").send_keys("CEO")
time.sleep(2)
driver.find_element_by_class_name("search-filter-typeahead__suggestion-item-value").click()
time.sleep(2)
driver.find_element_by_id("ember117").click()

driver.quit()
