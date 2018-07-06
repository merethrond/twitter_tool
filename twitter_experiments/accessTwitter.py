# !/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Jul  4 21:59:51 2018

# @author: tuffy
# """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from access_token import username, password
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)


# twitter login process
driver.get('https://twitter.com/login')
print(driver.title)
elem = driver.switch_to_active_element() # doesn't work always
# elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'session[username_or_email]')))

# elem = driver.find_element_by_name()
elem.send_keys(username)
elem.send_keys(Keys.TAB)
elem = driver.switch_to_active_element()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

#Get the access tokens of the already created apps.
driver.get('https://apps.twitter.com/')
elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
elem.click()
driver.get(driver.current_url[:-4] + "keys")

page_url = (driver.page_source)
tokenSoup = BeautifulSoup(page_url,"html.parser")#,"lxml")

# app_settings = tokenSoup.body.find('div', attrs={'class': 'app-settings'})

# divs = app_settings.find_all('div',attrs={'class':'row'})
# print(divs)

consumerKey = tokenSoup.select("div[class=app-settings] > div[class=row] > span[class=heading] > span")
print(consumerKey)
# driver.close()