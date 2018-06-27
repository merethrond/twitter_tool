from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
username = "ayushxx7@gmail.com"
password = "india2000" #values present in original file

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe')
driver.get(getdriver)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()

# after login there is a popup which should be closed
popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div/div/button[contains(., Close)]')))
driver.find_element_by_xpath("//div/div/button[contains(., Close)]").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Szr5J.coreSpriteHeartOpen')))
# find all 'hearts' presented on the page
likes = driver.find_elements(By.CSS_SELECTOR, ".Szr5J.coreSpriteHeartOpen")
print(len(likes))
print("WORKS")

for x in range(0,len(likes)):
    if likes[x].is_displayed():
        likes[x].click()
        print(x)