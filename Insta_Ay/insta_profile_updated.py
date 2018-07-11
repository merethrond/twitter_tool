import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from insta_key import password,username
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter

# from insta_beautiful_extraction import following_list

# #login credentials
# username = "xxxxxxxxx"
# password = "xxxxxxxxx"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)


def follower_extraction():

	following_list = pd.read_excel('following.xlsx')
	listname = following_list['babiabhalla'].unique()
	return listname

	# print(following_list)
	# # print(type(following_list))
	# print(following_list.keys())

	# for i in following_list.keys():
	# 	print(i)

# print(listname)	
# print(type(listname))

# for i in listname:
# 	print(i)

def login():
	login_page = ("https://www.instagram.com/accounts/login/")

	# driver = webdriver.Chrome(r"C:\Users\LakshayJuneja\Desktop\chromedriver.exe")
	driver.get(login_page)

	driver.find_element_by_name("username").send_keys(username)
	driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)
	driver.find_element_by_xpath("//button[contains(., 'Log in')]").click()
	time.sleep(5)
# time.sleep(5)

no_access_list = []

def profile_opener(following_list):
	print('opening profile:')
	for i in following_list:
		driver.get("https://www.instagram.com/"+i)
		liker(i)
	# driver.get("https://www.instagram.com/"+"punsworld")
	# liker()
	
		# time.sleep(6)

def liker(i):
	# time.sleep(2)
	try:
		first_image = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_9AhH0"]')))
		# first_image = driver.find_element_by_xpath('')
	except:
		print('unable to open image, shifting to next profile')
		no_access_list.append(i) 
		return 	

	account_num = 0
	print('going to account number',account_num)
	first_image.click()
	saccount_num+=1
	time.sleep(2)
	count = 0
	actions = ActionChains(driver)
	
	while count < 5:
		heart = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '//span[@class="fr66n"]')))
		# heart = driver.find_element_by_xpath('//span[@class="fr66n"]')
		if(heart.text) == "Like":
			print('liking image',count)
			heart.click()
		count += 1

		time.sleep(1)

		actions.send_keys(Keys.RIGHT)
		actions.perform()
		time.sleep(1.5)
	return	
		# right = driver.find_element_by_xpath('//a[@class="coreSpriteRightPaginationArrow"]')
		# right.click()
		# heart_children = heart.find_elements_by_css_selector("*")
	# heart = driver.find_element_by_xpath('//span[@class="fr66n"]')
	# heart_children = heart.find_elements_by_css_selector("*")
	# # print(heart_children)
	# for i in heart_children:
	# 	print("i",i.text)
	# print("heart",heart.text)	




login()	
following_list = follower_extraction()
profile_opener(following_list)

for i in no_access_list:
	print("Unable to access: ",i)

workbook = xlsxwriter.Workbook('notAccessible.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column('A1',no_access_list)
workbook.close()
	
# _9AhH0 - fist image of profile class
# def to_excel(credentials):
# df = pd.read_excel('following.xlsx', sheet_name = "Sheet1")

#     # list = [[access_token_secret,access_token,consumer_secret,consumer_key]]
# df = df.append(pd.DataFrame(credentials, columns=['Access Secret','Access Token','Consumer Secret','Consumer Token']),ignore_index=True)

# df.to_excel('filename.xlsx')
# print(df)

# fr66n - span class in feed/image of profile for heart
# for i in following_list:
# 	print(i)
#instagram account address
# user_acc = ("https://www.instagram.com/instagram/")
# driver.get(user_acc)


# user_profile = driver.find_element(By.CSS_SELECTOR,".Szr5J.kIKUG.coreSpriteDesktopNavProfile").click()


# img_urls = list();
# img_counter = 0

# #saving the image links
# img_divs = driver.find_elements_by_css_selector('div.v1Nh3>a')
# for img_div in img_divs:
# 	href = img_div.get_attribute('href')
# 	print(href)
# 	img_urls.append(href)
# 	img_counter += 1

# like = driver.find_elements(By.CSS_SELECTOR,".Szr5J.coreSpriteHeartOpen")

# #opening and liking the images
# for img_url in img_urls:
# 	print (img_url)
# 	driver.get(img_url)
# 	print ("Opening And Liking the Image......")
# 	time.sleep(2)
# 	for x in range(0,len(like)):
# 		if like[x].is_displayed():
# 			like[x].click()
# 	time.sleep(2)
# 	print ("Done!!")



# for i in range(0,10):
# 	time.sleep(20)
# 	like = driver.find_elements(By.CSS_SELECTOR,".Szr5J.coreSpriteHeartOpen")
# 	for x in range(0,len(like)):
# 		if like[x].is_displayed():
# 			like[x].click()