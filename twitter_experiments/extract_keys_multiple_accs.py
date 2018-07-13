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
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

from access_token_extraction_library import login_to_twitter, get_keys_of_first_app,\
create_app, to_excel, delete_first_app

from excelReader import credentials

def create_apps_save_keys():
    app_name_index = 0
    for username in credentials.keys():
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        login_to_twitter(driver, username, credentials[username])
        create_app(driver, "trial__" + str(app_name_index))
        to_excel(get_keys_of_first_app(driver), username)
        driver.close()
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
    df = read_excel("filename.xlsx")
    for username in df.username:
        driver = webdriver.Chrome(executable_path = DRIVER_BIN)
        login_to_twitter(driver, username, credentials[username])
        time.sleep(10)
# delete_multiple_apps()
# create_apps_save_keys()
login_and_wait()
# collect_keys_multiple_apps()
