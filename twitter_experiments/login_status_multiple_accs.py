from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd
from vault import login_excel
excel_data = pd.read_excel(email_excel)
'''
Use this in case of windows.
'''
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
'''
In case of mac.
'''
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")

'''
In case of windows.
'''

# driver = webdriver.Chrome(executable_path = DRIVER_BIN)

# driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
# driver.get(account)
# signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
# signIn.click()
# print("Twitter app opened")

#Current account active status
# issues = ['not active', 'active', 'active', 'not active', 'active', 'active', 'active', 'active', 'not active']
issues = []
account =('https://apps.twitter.com/')
for username, password in zip(excel_data.username, excel_data.password):
   driver = webdriver.Chrome(executable_path = DRIVER_BIN)
	# driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
   time.sleep(1)
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

   time.sleep(1)
   email = driver.switch_to_active_element()
	# passcode = driver.find_element_by_name("session[password]")
   email.send_keys(password)
   email.send_keys(Keys.RETURN)
   print("password entered")

   time.sleep(2)
	# LogIn = driver.find_element_by_xpath('//input[@type="submit"]')
	# LogIn.click()
   print("Logged in")
#    print("URL:" + driver.current_url)
   if driver.current_url == 'https://apps.twitter.com/':
       issues.append("active")
   else:
       issues.append("not active")
#    issues.append(driver.current_url)

   driver.close()
#
excel_data['issues'] = issues
print(issues)
excel_data.to_excel(email_excel)
print(excel_data)
