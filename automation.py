# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import yaml

conf = yaml.safe_load(open('loginDetails.yml'))
# variables
dis = conf['user_info']['user']
dis_pw = conf['user_info']['password']
url = 'https://dc80sci.riteaid.com/sci/bi/'
dropdown = 'mip'

# fetch browser wait for load
browser = webdriver.Chrome()
browser.get((url))
time.sleep(5)

# sign in with delay inputs
select = Select(browser.find_element(By.NAME, 'CAMNamespace'))
select.select_by_value(dropdown)
time.sleep(1)
username = browser.find_element(By.ID, 'CAMUsername')
username.send_keys(dis)
time.sleep(1)
password = browser.find_element(By.ID, 'CAMPassword')
password.send_keys(dis_pw)
time.sleep(1)
signInButton = browser.find_element(By.CLASS_NAME, 'signInBtn')
signInButton.click()
time.sleep(10)

#find our element
mySearch = browser.find_element(By.ID, 'com.ibm.bi.search.search')
mySearch.click()
time.sleep(5)

mySearch.send_keys('inventory adjustment')
