import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#login credentials
username = "xxxxxxxxx"
password = "xxxxxxxxx"

login_page = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome(r"C:\Users\LakshayJuneja\Desktop\chromedriver.exe")
driver.get(login_page)

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(., 'Log in')]").click()
time.sleep(5)

#instagram account address
user_acc = ("https://www.instagram.com/instagram/")
driver.get(user_acc)

img_urls = list();
img_counter = 0

#saving the image links
img_divs = driver.find_elements_by_css_selector('div.v1Nh3>a')
for img_div in img_divs:
	href = img_div.get_attribute('href')
	print(href)
	img_urls.append(href)
	img_counter += 1

like = driver.find_elements(By.CSS_SELECTOR,".Szr5J.coreSpriteHeartOpen")

#opening and liking the images
for img_url in img_urls:
	print (img_url)
	driver.get(img_url)
	print ("Opening And Liking the Image......")
	time.sleep(2)
	for x in range(0,len(like)):
		if like[x].is_displayed():
			like[x].click()
	time.sleep(2)
	print ("Done!!")



# for i in range(0,10):
# 	time.sleep(20)
# 	like = driver.find_elements(By.CSS_SELECTOR,".Szr5J.coreSpriteHeartOpen")
# 	for x in range(0,len(like)):
# 		if like[x].is_displayed():
# 			like[x].click()
