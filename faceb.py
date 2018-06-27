from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)

username = '9312645200'
password = 'india2000'

# def super_get(url):
#     driver.get(url)
#     driver.execute_script("window.alert = function() {};")

#driver = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('http://www.facebook.com/login')
# super_get('http://www.facebook.com/login')

driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(password)
driver.find_element_by_name('login').click()
time.sleep(2)
#driver.find_elements_by_name('q').send_keys('Ayush Mandowara')	
driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys('Ayush Mandowara' + Keys.RETURN)
time.sleep(4)
driver.find_element_by_xpath('//div[contains(text(), "Ayush Mandowara")]').click()
time.sleep(3)
driver.find_element_by_class_name('coverBorder').click()
time.sleep(2)
driver.find_element_by_xpath('//span[contains(text(), "Like")]').click()


