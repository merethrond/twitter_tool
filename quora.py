from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains


username = "alamgirakmal@gmail.com"
password = "desperateforsolace"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Admin\Desktop\chromedriver.exe', chrome_options=chrome_options)
driver.get('https:/www.quora.com')
time.sleep(5)

before = driver.window_handles[0]
time.sleep(10)
driver.find_element_by_class_name("google_button_text").click()
time.sleep(5)
# WebDriverWait(driver, timeout = 50).until(found_window("Sign in - Google Accounts-Google Chrome"))
after = driver.window_handles[1]
driver.switch_to_window(after)

driver.find_element_by_name("identifier").send_keys(username+Keys.RETURN)
time.sleep(10)
driver.find_element_by_name("password").send_keys(password+Keys.RETURN)
time.sleep(5)
driver.switch_to_window(before)
# driver.get('https:/www.quora.com/profile/Ayush-Mandowara')
time.sleep(5)
# driver.find_element_by_xpath("//input[@placeholder= 'Search Quora']").send_keys("Akmal Alamgir" + Keys.RETURN)
# search = driver.find_element_by_xpath("//textarea[@name='selector_input text']")
# search.send_keys("AKMAL ALAMGIR");
search = driver.find_element(By.CSS_SELECTOR, ".selector_input.text" ).click()
search.send_keys("AKMAL ALAMGIR");