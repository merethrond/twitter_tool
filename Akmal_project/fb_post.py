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

 
username = "alamgirakmal@yahoo.com"
Password = "desperateforsolace"

account =('https://www.facebook.com/login.php?login_attempt=1&lwv=110')

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Admin\Desktop\chromedriver.exe', chrome_options=chrome_options)

# driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\chromedriver.exe")
driver.get(account)

print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(username)
print("email entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(Password)
print("Password entered...")
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("facebook opened")
status= driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
status.send_keys("Lets check how it goes by..");
print("Status typing")
time.sleep(5)
driver.find_element_by_xpath("//button[contains(., 'Post')]").click()
# driver.find_element(By.CSS_SELECTOR,"._1mf7._4r1q._4jy0._4jy3._4jy1._51sy.selected _42ft").click()
print("post done")