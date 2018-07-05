#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:59:51 2018

@author: tuffy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from access_keys import username, password
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

# twitter login process
driver.get('https://twitter.com/login')
print(driver.title)
elem = driver.switch_to_active_element()
elem.send_keys(username)
elem.send_keys(Keys.TAB)
elem = driver.switch_to_active_element()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

#Get the access tokens of the already created apps.
driver.get('https://apps.twitter.com/')
elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
elem.click()
#driver.close()