from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

# from excelReader import credentials
from vault import user_keys_excel


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
    account = 'https://apps.twitter.com/'
    driver.get(account)
    signIn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]')))
    # signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
    signIn.click()
    print("Username:", username)
    print("Twitter app opened")
    time.sleep(2)
    email = driver.switch_to_active_element()
    email.send_keys(username)
    email.send_keys(Keys.TAB)
    print("email entered")

    time.sleep(1)
    password_field = driver.switch_to_active_element()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    print("password entered")

    time.sleep(1)
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

def create_or_get_keys(driver, app_name, username):
    driver.get('https://apps.twitter.com/')
    try:
        elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    except:
        create_app(driver, app_name)
    to_excel(get_keys_of_first_app(driver), username)

    driver.close()
    # print(type(elem))


def to_excel(credential_list, username):
    df = pd.read_excel(access_keys_excel, sheet_name = "Sheet1")

    try:
        df_index = int(df[df.username == username].index.to_native_types()[0])
        df.loc[df_index, 'consumer_key'] = credential_list[0]
        df.loc[df_index, 'consumer_secret'] = credential_list[1]
        df.loc[df_index, 'access_token'] = credential_list[2]
        df.loc[df_index, 'access_token_secret'] = credential_list[3]

    except IndexError:
        df = df.append(pd.DataFrame([[username] + credential_list], columns=['username','consumer_key','consumer_secret','access_token','access_token_secret']),ignore_index=True)

    df.to_excel(access_keys_excel)
    print(df)



def delete_first_app(driver, username):
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
        #Removing the username entry from the excel file.
        #This will remove multiple entries as well.
        df = pd.read_excel(access_keys_excel, sheet_name = "Sheet1")
        df = df[df.username != username]
        df.to_excel(access_keys_excel)


    except:
        print("Error: No app found, or error in excel deletion.")

    # driver.close()
def delete_from_excel(username):
    df = pd.read_excel(access_keys_excel, sheet_name = "Sheet1")
    df = df[df.username != username]
    df.to_excel(access_keys_excel)


# login_to_twitter(driver, username, password)
# delete_first_app(driver, username)
# create_app(driver, app_name = 'trial___1')
#to_excel(get_keys_of_first_app(driver), username)
# print(get_keys_of_first_app(driver))
#delete_from_excel(username)
# create_or_get_keys(driver, app_name = "trail___1")
