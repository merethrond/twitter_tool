from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq 
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains

# from access_keys import username, password 
from excelReader import credentials
account =('https://apps.twitter.com/')
'''
Use this in case of windows.
'''
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)

# import os
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

# driver = webdriver.Chrome(executable_path = DRIVER_BIN)

# driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
# driver.get(account)
# signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
# signIn.click()
# print("Twitter app opened")



for username in credentials:

	driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
	time.sleep(3)	
	driver.get(account)
	signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
	signIn.click()
	print("Twitter app opened")

	email = driver.switch_to_active_element()
	time.sleep(3)
	# email = driver.find_element_by_class_name("swift-loading no-nav-banners")
	email.send_keys(username)
	email.send_keys(Keys.TAB)
	print("email entered")

	time.sleep(3)
	email = driver.switch_to_active_element()
	# passcode = driver.find_element_by_name("session[password]")
	email.send_keys(credentials[username])
	email.send_keys(Keys.RETURN)
	print("password entered")


	time.sleep(2)
	# LogIn = driver.find_element_by_xpath('//input[@type="submit"]')
	# LogIn.click()
	print("Logged in")

	driver.close()

# New_app = driver.find_element_by_xpath("//a[@href ='/app/new']")
# New_app.send_keys(Keys.RETURN)

# name = driver.find_element_by_name("name")
# name.send_keys("John Abraham")
# name.send_keys(Keys.TAB)

# description = driver.switch_to_active_element()
# description.send_keys("Force and Rocky handsome")
# description.send_keys(Keys.TAB)

# website = driver.switch_to_active_element()
# website.send_keys("https://www.google.com")
# time.sleep(1)

# website.send_keys(Keys.TAB)
# time.sleep(1)

# Oauth = driver.switch_to_active_element()
# Oauth.send_keys(Keys.TAB)
# time.sleep(1)

# URL = driver.switch_to_active_element()
# URL.send_keys(Keys.TAB)
# time.sleep(1)

# URL_Tab = driver.switch_to_active_element()
# URL_Tab.send_keys(Keys.TAB)
# time.sleep(1)

# Confirm = driver.switch_to_active_element()
# Confirm.send_keys(Keys.SPACE)
# Confirm.send_keys(Keys.TAB)
# time.sleep(1)

# link = driver.switch_to_active_element()
# link.send_keys(Keys.TAB)
# time.sleep(1)


# Create = driver.switch_to_active_element()
# Create.send_keys(Keys.RETURN)
# print(driver.current_url)
# Akmal_app = driver.find_element_by_xpath("//a[@href ='app/15260788/show']").click()
# time.sleep(5)
# driver.find_element_by_xpath('//div[contains(text(), "Keys and Access Tokens")]').click()
driver.get(driver.current_url + "/keys")
# page = (driver.page_source)

get_access = driver.find_element_by_name("op")
get_access.click()

