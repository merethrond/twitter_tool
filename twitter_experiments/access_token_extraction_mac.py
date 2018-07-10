#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:59:51 2018

@author: tuffy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

from access_keys import username, password

#from access_token import username, password

from bs4 import BeautifulSoup

#Abhishek
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")
#driver = webdriver.Chrome(executable_path = DRIVER_BIN)

#Akmal
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(r'C:\Users\Admin\Desktop\chromedriver.exe', chrome_options=chrome_options)

#Ayush
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)


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
    #comment out the line below in case you want to leave the browser open after calling this function.
    # driver.close()

    tokenSoup = BeautifulSoup(page,"html.parser")#,"lxml")
    consumer_tokens = tokenSoup.select(".app-settings > .row > span")
    consumer_key = consumer_tokens[1].string
    consumer_secret = consumer_tokens[3].string
    print("consumer_key:", consumer_key, "consumer_secret:", consumer_secret, sep = '\n')
    try:
        get_access = driver.find_element_by_name("op")
        get_access.click()
        time.sleep(10)
        driver.refresh()
    except:
        print("No access button found")

    page = (driver.page_source)
    tokenSoup = BeautifulSoup(page,"html.parser")#,"lxml")
    access_tokens = tokenSoup.select(".access > .row > span")
    print(access_tokens)
    access_token = access_tokens[1].string
    access_token_secret = access_tokens[3].string
    print("access_token:", access_token, "access_token_secret:", access_token_secret, sep = '\n')

    credential_list = [[access_token_secret,access_token,consumer_secret,consumer_key]]

    return credential_list


def create_app(driver):
    driver.get('https://apps.twitter.com/')

    New_app = driver.find_element_by_xpath("//a[@href ='/app/new']")
    New_app.send_keys(Keys.RETURN)

    name = driver.find_element_by_name("name")
    name.send_keys("mai pro hun")
    name.send_keys(Keys.TAB)

    description = driver.switch_to_active_element()
    description.send_keys("All the new films")
    description.send_keys(Keys.TAB)

    website = driver.switch_to_active_element()
    website.send_keys("https://www.google.com")
    time.sleep(1)

    website.send_keys(Keys.TAB)
    time.sleep(1)

    Oauth = driver.switch_to_active_element()
    Oauth.send_keys(Keys.TAB)
    time.sleep(1)

    URL = driver.switch_to_active_element()
    URL.send_keys(Keys.TAB)
    time.sleep(1)

    URL_Tab = driver.switch_to_active_element()
    URL_Tab.send_keys(Keys.TAB)
    time.sleep(1)

    Confirm = driver.switch_to_active_element()
    Confirm.send_keys(Keys.SPACE)
    Confirm.send_keys(Keys.TAB)
    time.sleep(1)

    link = driver.switch_to_active_element()
    link.send_keys(Keys.TAB)
    time.sleep(1)


    Create = driver.switch_to_active_element()
    Create.send_keys(Keys.RETURN)



def to_excel(credentials):
    df = pd.read_excel('filename.xlsx', sheet_name = "Sheet1")

    # list = [[access_token_secret,access_token,consumer_secret,consumer_key]]
    df = df.append(pd.DataFrame(credentials, columns=['Access Secret','Access Token','Consumer Secret','Consumer Token']),ignore_index=True)

    df.to_excel('filename.xlsx')
    print(df)


def delete_first_app(driver):
    driver.get('https://apps.twitter.com/')
    elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    elem.click()
    driver.get(driver.current_url[:-4] + "delete")
    elem = driver.find_element_by_name("op")
    time.sleep(4)
    elem.click()
    time.sleep(4)

#login_to_twitter(driver)
#delete_first_app(driver)
#create_app(driver)
#to_excel(get_keys_of_first_app(driver))
