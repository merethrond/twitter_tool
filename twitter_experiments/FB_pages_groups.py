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


username = "alamgirakmal@yahoo.com"
Password = "desperateforsolace"
account = ("https://en-gb.facebook.com/login/")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Admin\Desktop\chromedriver.exe', chrome_options=chrome_options)
driver.get(account)
time.sleep(3)

driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(Password)
driver.find_element_by_name("login").click()
# driver.find_elements_by_class_name("_1frb").send_keys("Hrithik Roshan" + Keys.RETURN)
# driver.find_elements_by_class_name("_4xj-").click()
time.sleep(3)
driver.find_element_by_xpath('//input[@placeholder= "Search"]').send_keys("Jaby Koay" + Keys.RETURN)

#pages = driver.find_element_by_class_name("_4xjz")
#pages.click()

# time.sleep(10)
# firstresult = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Jaby Koay")]')))
firstresult = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._52eh')))

#firstresult = driver.find_element_by_xpath('//div[contains(text(), "Jaby Koay")]')
# firstresult = driver.find_element_by_css_selector("._52eh")

firstresult.click() 
time.sleep(5)
# like = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.likeButton._4jy0._4jy4._517h._51sy._42ft')))
# like = driver.find_element(By.CSS_SELECTOR, '.likeButton._4jy0._4jy4._517h._51sy._42ft')
# like.click()

follow = driver.find_element(By.CSS_SELECTOR, '._4jy0._4jy4._517h._51sy._42ft')
follow.click()


time.sleep(7)

# post = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1mf._1mj')))
# post = driver.find_element(By.CSS_SELECTOR, '._1mf._1mj')
# post = driver.find_element(By.CSS_SELECTOR, '.notranslate._5rpu')
# post = driver.find_element_by_xpath('//input[@placeholder= "Write something on this Page..."]')
post = driver.find_elements_by_class_name("_5qtp")

time.sleep(2)
post[1].click()


time.sleep(2)
# post[0].click()

time.sleep(2)
post_now = driver.switch_to_active_element()
post_now.send_keys("Your AIB reactions rock")
# pic = post_now.send_keys(Keys.TAB)
# time.sleep(1)
# pic = driver.find_element_by_class_name("_3jk")

# pic.send_keys(Keys.TAB)



# # pic = driver.switch_to_active_element()
# people = pic.send_keys(Keys.TAB)
# time.sleep(1)
# # people = driver.switch_to_active_element()
# loc = people.send_keys(Keys.TAB)
# time.sleep(1)
# # loc = driver.switch_to_active_element()
# loc.send_keys(Keys.TAB)
# time.sleep(1)
# button = driver.switch_to_active_element()
# button.click()

# button = driver.find_element_by_xpath('//button[contains(text(), "Post")]')
# button.click()

# post = driver.find_element_by_css_selector("._5rp7")
# post = driver.find_element_by_css_selector("._1p1t")

# post[0].send_keys("I am very fond of your reaction videos.")

# time.sleep(5)
# button = driver.find_element_by_xpath("//button[contains(., 'Post')]")
# button.click()
# time.sleep(4)

# driver.find_element_by_xpath('//div[contains(text(), "Akmal Alamgir")]').click()
# searchbox = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, 'q'))).click()
# searchbox.click()
# driver.find_element_by_name('q').send_keys('Ayush Mandowara' + Keys.RETURN)	
# searchbox.send_keys('Ayush Mandowara' + Keys.RETURN)

# ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# searchbox = WebDriverWait(driver, 35,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.NAME, 'q')))
# searchbox.click()
# searchbox.send_keys('AKMAL ALAMGIR' + Keys.RETURN)

