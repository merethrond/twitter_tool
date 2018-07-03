from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions    import NoSuchWindowException

driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe')

driver.get('http://www.quora.com')

username = "_"
password = "_" #put your google username and password here


### FOUND WINDOW CODE

def found_window(name):
    def predicate(driver):
        try: driver.switch_to_window(name)
        except NoSuchWindowException:
             return False
        else:
             return True # found window
    return predicate

time.sleep(2)
before = driver.window_handles[0]
driver.find_element_by_class_name("google_button_text").click()
time.sleep(3)
# print(driver.window_name
# WebDriverWait(driver, timeout=50).until(found_window("Sign in - Google Accounts - Google Chrome"))

after = driver.window_handles[1]
driver.switch_to_window(after)
# action = ActionChains(driver)
# action.send_keys(username)
# # +Keys.RETURN
# action.perform()
driver.find_element_by_name('identifier').send_keys(username+Keys.RETURN)
time.sleep(2)
driver.find_element_by_name('password').send_keys(password+Keys.RETURN)
time.sleep(2)
driver.switch_to_window(before)
time.sleep(2)
# driver.find_element_by_xpath('//textarea[@placeholder="Search Quora"]').send_keys('Amrit Singh' + Keys.RETURN)
# driver.find_element(By.CSS_SELECTOR, '.selector_input.text').send_keys('Amrit Singh'+Keys.RETURN)
# driver.get('https://www.quora.com/profile/Amrit-Singh-94')

driver.get('https://www.quora.com/profile/Lakshya-Aggrawal') #upvoting this profile's answers

# upvotes = driver.find_elements_by_xpath('//span[contains(text(),"Upvote")]')
# upvotes = driver.find_elements_by_xpath('//a[@action_click="AnswerUpvote"]')
 # and contains(text(),"Upvote")')

# print(upvotes)

# for i in range(0,3):
# 	for i in range(0,len(upvotes)):
# 		try:
# 			if upvotes[i].is_displayed:
# 				upvoted = upvote[i].get_attribute("action_click")
# 				print(upvoted)
# 				# if (upvotes[i].get_attribute("action_click"))=="AnswerRemoveUpvote":
# 				# 	print('already upvoted')
# 				# else:	
# 				upvotes[i].click()
# 		except:
# 			print('Element',upvotes[i],'not clickable. Skipping!')
# 			pass		
	#selector_input text
# time.sleep(5)

####### UPVOTER

for i in range(0,10):
	time.sleep(4)
	upvotes = driver.find_elements_by_xpath('//a[@action_click="AnswerUpvote"]') #better approach to only upvote answers that have't been upvoted
	print(upvotes)
	for i in range(0,len(upvotes)):
		try:
			if upvotes[i].is_displayed:
				# upvoted = upvote[i].get_attribute("action_click")
				# print(upvoted)
				upvotes[i].click()
		except:
			print('Element',upvotes[i],'not clickable. Skipping!')
			pass		

#### SHARE

# class="ItemComponent QuoraShareActionItem ActionItemComponent action_item"

### INSTA image class on opening profile possibly is: eLAPa

# print(upvotes[0].get_attribute('action_click'))
# parentElem = upvotes[0].find_element_by_xpath(".//ancestor::a")






#driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
# need to use xpath because input

