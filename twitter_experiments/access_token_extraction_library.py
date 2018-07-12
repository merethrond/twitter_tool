from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

# from access_keys import username, password
#from access_token import username, password
# from excelReader import credentials

from bs4 import BeautifulSoup

# Abhishek
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")
# driver = webdriver.Chrome(executable_path = DRIVER_BIN)

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
def login_to_twitter(driver, username, password):
    # driver.get('https://twitter.com/login')
    # print(driver.title)
    # elem = driver.switch_to_active_element()
    # elem.send_keys(username)
    # elem.send_keys(Keys.TAB)
    # elem = driver.switch_to_active_element()
    # elem.send_keys(password)
    # elem.send_keys(Keys.RETURN)

    account = 'https://apps.twitter.com/'
    time.sleep(1)
    driver.get(account)
    signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
    signIn.click()
    print("Username:", username)
    print("Twitter app opened")

    email = driver.switch_to_active_element()
    time.sleep(1)
    email.send_keys(username)
    email.send_keys(Keys.TAB)
    print("email entered")

    time.sleep(1)
    email = driver.switch_to_active_element()
    email.send_keys(password)
    email.send_keys(Keys.RETURN)
    print("password entered")

    time.sleep(2)
    print("Logged in")
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
    # print(access_tokens)
    access_token = access_tokens[1].string
    access_token_secret = access_tokens[3].string
    print("access_token:", access_token, "access_token_secret:", access_token_secret, sep = '\n')

    credential_list = [consumer_key,consumer_secret,access_token,access_token_secret]

    return credential_list


def create_app(driver, app_name):
    driver.get('https://apps.twitter.com/')

    New_app = driver.find_element_by_xpath("//a[@href ='/app/new']")
    New_app.send_keys(Keys.RETURN)

    name = driver.find_element_by_name("name")
    name.send_keys(app_name)
    name.send_keys(Keys.TAB)

    description = driver.switch_to_active_element()
    description.send_keys("Trying out the twitter APIs")
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



def to_excel(credential_list, username):
    df = pd.read_excel('filename.xlsx', sheet_name = "Sheet1")

    df = df.append(pd.DataFrame([[username] + credential_list], columns=['username','consumer_key','consumer_secret','access_token','access_token_secret']),ignore_index=True)

    df.to_excel('filename.xlsx')
    print(df)



def delete_first_app(driver):
    driver.get('https://apps.twitter.com/')
    try:
        elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
        elem.click()
        driver.get(driver.current_url[:-4] + "delete")
        elem = driver.find_element_by_name("op")
        time.sleep(4)
        elem.click()
        time.sleep(4)
        print("App deleted")
    except:
        print("Error: No app found")

    # driver.close()


# login_to_twitter(driver, username, password)
# delete_first_app(driver)
# create_app(driver, app_name = 'trial___1')
# to_excel(get_keys_of_first_app(driver), username)
# print(get_keys_of_first_app(driver))
