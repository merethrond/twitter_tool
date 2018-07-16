from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from fb_credentials import username,Password

account = ("https://en-gb.facebook.com/login/")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
driver.get(account)
# (?# driver.get(r'C:\Users\Admin\Desktop\modi.html'))
time.sleep(3)

driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(Password)
driver.find_element_by_name("login").click()
# driver.find_elements_by_class_name("_1frb").send_keys("Hrithik Roshan" + Keys.RETURN)
# driver.find_elements_by_class_name("_4xj-").click()
time.sleep(3)
driver.find_element_by_xpath('//input[@placeholder= "Search"]').send_keys("Modi" + Keys.RETURN)

time.sleep(5)

group = driver.find_elements_by_class_name('_3m1v')
group[7].click()

group_url = driver.current_url
time.sleep(5)



# finds_children = []
# finds = driver.find_elements_by_css_selector("._52eh._5bcu")
# print(len(finds))
# fol_list = driver.find_elements_by_xpath("//div[@role='dialog']//li//a")
# href = img_div.get_attribute('href')
# 	print(href)
href_list = []

# driver.findElement(By.partialLinkText("here")).click();	
finds = driver.find_elements_by_xpath('//div[@class="_ajw"]')
for i in finds:
	# href = i.find_element_by_xpath('//div//div//a')
	href = i.find_elements_by_xpath(".//a")
	# href_list.append(href.get_attribute('href'))
	for i in href:
		print('\n####',i.text)
		print('#href',i.get_attribute('href'),'#')
		href_list.append(i.get_attribute('href'))

print(href_list)
for i in href_list:
	driver.get(i)
	time.sleep(6)
# 	
# try:	
# 		# i.click()
# 		time.sleep(4)
# 		driver.execute_script("arguments[0].click();", i)
# 		print('clicked')
# 		time.sleep(4)
# 		print(driver.current_url)
# 		print(group_url)
# 		driver.get(group_url)
# 	except:
# 		print('could not click')
# 		pass	
# # for child in finds:
# 	finds_children.append(child.find_element_by_tag_name('a'))
# for i in finds_children:
# 	print(i)
# 	print(i.text)
# 	i.click()
	

# finds = driver.find_element_by_xpath('//div[contains(text(), "Aam Aadmi Party")]')
# counter = 0
# print(len(finds))
# for i in finds:
# 	if(counter%2==0):
# 		print('########')
# 		print(i.text)
# 	counter += 1	
# finds.click()

# finds = driver.find_elements_by_class_name('_52eh')
# finds[0].click()
# join_list = driver.find_elements_by_xpath('//i[contains(text,"Join")]')
# group[7].send_keys(Keys.END)
# group[7].send_keys(Keys.END)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# totalrequest = 0

# for i in range(5):
# 	sentcount = 0
# 	join_list = driver.find_elements_by_css_selector('._42ft._4jy0._4jy3._517h._51sy')

# 	print(len(join_list))
# 	# print(join_list)
# 	# for i in join_list:
# 	# 	print(i.text)

# 	for i in join_list:
# 		print(i.text)
# 		try:
# 			if(i.text == 'Join'):
# 			# i.click()
# 				driver.execute_script("arguments[0].click();", i)
# 				sentcount += 1	
# 				totalrequest += 1
# 				# try:
# 				# 	time.sleep(3)
# 				# 	answer_for_group = driver.find_element_by_xpath('//textarea[title="Write an answer..."]')
# 				# 	# for i in answer_for_group:

# 				# 	answer_for_group.send_keys('I am a big fan of Aam Aadmi Party, Arvind Sir is doing a good job! Hope he wins in all future elections! He has done a great job in Delhi!')
# 				# except:
# 				# 	print('nahi mila khushi hai')
# 				# 	pass		
# 		except:
# 			print('hamse na ho payega')
# 			pass
# 	driver.refresh()
# 	print('Request Sent:',sentcount)
# 	print('Total Request Sent:',totalrequest)

# time.sleep(5)
'''
textarea title="Write an answer..."
<textarea title="Write an answer..." class="uiTextareaAutogrow _vxq" rows="3" maxlength="250" name="questionnaire_answers[]" placeholder="Write an answer..." aria-labelledby="u_3k_0" id="u_3k_7" style="height: 60px;">I am a big fan</textarea>
'''
# JoinButton = driver.find_elements_by_class_name("_42ft ")
# JoinButton[4].click()
# driver.find_element_by_xpath("//button[contains(., 'Join Group')]")