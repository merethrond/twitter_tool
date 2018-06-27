from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
username = "ayushxx7@gmail.com"
password = "india2000"

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe')
driver.get(getdriver)
driver.maximize_window()

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# browser = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe')
# browser.get('http://www.instagram.com/')

#time.sleep(5)

for i in range(0,10):
	time.sleep(5)
	like = driver.find_elements(By.CSS_SELECTOR, ".Szr5J.coreSpriteHeartOpen")
	for x in range(0,len(like)):
	    if like[x].is_displayed():
	        like[x].click()

