#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:59:51 2018

@author: tuffy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

import os
from access_keys import username, password
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

# twitter login process
def login_to_twitter(driver):
    driver.get('https://twitter.com/login')
    print(driver.title)
    #elem = WebDriverWait(driver, 30).presence_of_element_located(By.NAME, "session")
    elem = driver.switch_to_active_element()
    #elem = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'session[username_or_email]')))
    elem.send_keys(username)
    elem.send_keys(Keys.TAB)
    elem = driver.switch_to_active_element()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

#Get the access tokens of the already created apps.
def get_keys_of_first_app(driver):
    driver.get('https://apps.twitter.com/')
    elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    elem.click()
    driver.get(driver.current_url[:-4] + "keys")
    page = (driver.page_source)
    driver.close()
    tokenSoup = BeautifulSoup(page,"html.parser")#,"lxml")
    consumer_tokens = tokenSoup.select(".app-settings > .row > span")
    consumer_key = consumer_tokens[1].string
    consumer_secret = consumer_tokens[3].string
    print("consumer_key:", consumer_key, "consumer_secret:", consumer_secret, sep = '\n')
    access_tokens = tokenSoup.select(".access > .row > span")
    access_token = access_tokens[1].string
    access_token_secret = access_tokens[3].string
    print("access_token:", access_token, "access_token_secret:", access_token_secret, sep = '\n')

    
login_to_twitter(driver)
get_keys_of_first_app(driver)    
