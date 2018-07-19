#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:13:38 2018

@author: tuffy
"""
import os
import time
from pandas import read_excel
from selenium import webdriver
from vault import login_excel
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

from access_token_extraction_library import login_to_twitter, get_keys_of_first_app,\
create_app, to_excel, delete_first_app, create_or_get_keys

from excelReader import credentials

def create_apps_save_keys():
    app_name_index = 0
    for username in credentials.keys():
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        login_to_twitter(driver, username, credentials[username])
        create_or_get_keys(driver, "trial__" + str(app_name_index), username)
        # driver.close()
        app_name_index += 1
def delete_multiple_apps():
    for username in credentials.keys():
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        login_to_twitter(driver, username, credentials[username])
        delete_first_app(driver, username)
        driver.close()

def collect_keys_multiple_apps():
    for username in credentials.keys():
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        login_to_twitter(driver, username, credentials[username])
        to_excel(get_keys_of_first_app(driver), username)
        driver.close()
def login_and_wait():
    """
    Note: Login is done on only those credentials whose access details are there.
    """
    df = read_excel(access_keys_excel)
    # for username in credentials.keys():
    for username in df.username:
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        login_to_twitter(driver, username, credentials[username])
        driver.get("http://www.twitter.com")
    time.sleep(30)
# delete_multiple_apps()
# create_apps_save_keys()
login_and_wait()
# collect_keys_multiple_apps()
