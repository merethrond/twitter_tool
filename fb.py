from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

# from pynput.keyboard import Key, Controller

# import keyboard

# keyboard = Controller()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)

username = '---'
password = '---'

# def super_get(url):
#     driver.get(url)
#     driver.execute_script("window.alert = function() {};")

#driver = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('http://www.facebook.com/login')
# super_get('http://www.facebook.com/login')

driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(password)
driver.find_element_by_name('login').click()
# time.sleep(2)
driver.maximize_window()
#driver.find_elements_by_name('q').send_keys('Ayush Mandowara')	
driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys('Ayush Mandowara' + Keys.RETURN)
time.sleep(4)
driver.find_element_by_xpath('//div[contains(text(), "Ayush Mandowara")]').click()
time.sleep(3)
driver.find_element_by_class_name('coverBorder').click()
time.sleep(2)

####LIKE
# for i in range(0,10):
# 	like = driver.find_elements(By.CSS_SELECTOR, ".UFILikeLink._4x9-._4x9_._48-k")
# 	x = len(like)-1
# 	print(like[x])
# 	liked = like[x].get_attribute("data-testid")
# 	print(liked)
# 	if liked == "fb-ufi-likelink":
# 		like[x].click()
# 	actions = ActionChains(driver)
# 	actions.send_keys(Keys.RIGHT)
# 	actions.perform()
# 	time.sleep(2)

# driver.execute_script("var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');for(var i= 0;i<elems.length;i++){elems[i].click();}");


### COMMENT

# comment = driver.find_elements(By.CSS_SELECTOR, ".comment_link._5yxe")
# x = len(comment)-1
# comment[x].click()
# time.sleep(2)
# actions = ActionChains(driver)
# actions.send_keys('dummydata')
# actions.perform()

### SHARE

# share = driver.find_elements(By.CSS_SELECTOR, ".share_action_link._5f9b")
# x = len(share)-1
# share[x].click()
# time.sleep(4)
# element = driver.find_element_by_xpath("//button[contains(.,'Post')]")
# print(element)
# element.click()
# share_action_link _5f9b

# actions = ActionChains()
# keyboard.write('The quick brown fox jumps over the lazy dog.')
# keyboard.type('Hello World')

# comment[x].send_keys('')
# y = comment[x].click()
# y.send_keys('asd')
# for x in range(0,len(comment)):
# 	    if comment[x].is_displayed():
# 	        comment[x].click()
# element = driver.find_element_by_xpath('//a[contains(text(), "Like")]')
# driver.find_element_by_class_name('coverBorder').send_keys("l")
# print(element)
# driver.execute_script("arguments[0].click();", element)
# element = driver.find_element_by_xpath("//button[contains(.,'comment')]")

# element = driver.find_element_by_xpath('//input[@placeholder="Write a comment..."]').send_keys('pro')
# element.click()
'''
if file name is selenium there will be error

FACEBOOK CLASS:
<div class="_524d"><div class="_42nr _1mtp"><span class="_1mto"><div class="_khz _4sz1 _4rw5 _3wv2"><a aria-pressed="true" class="UFILikeLink _4x9- _4x9_ _48-k UFILinkBright" data-testid="fb-ufi-unlikelink" href="#" role="button" tabindex="0" style="color: rgb(53, 120, 229);">Like</a><div class="_2r6l accessible_elem"><div class="_1oxj uiLayer hidden_elem" style="opacity: 1; left: 499px; top: 358px; z-index: 301;"><div class="_49v-"><div height="52" class="_1oxk"><div class="_iu- _628b _1ef3" data-testid="UFIReactionsMenu" aria-label="Reactions" role="toolbar"><span aria-pressed="true" aria-label="Like" class="_iuw" data-testid="reaction_1" href="#" role="button" tabindex="0"><div class="_39m _1ef2" data-reaction="1"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Like</div></div></div></div></span><span aria-pressed="false" aria-label="Love" class="_iuw" data-testid="reaction_2" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="2"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Love</div></div></div></div></span><span aria-pressed="false" aria-label="Haha" class="_iuw" data-testid="reaction_4" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="4"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Haha</div></div></div></div></span><span aria-pressed="false" aria-label="Wow" class="_iuw" data-testid="reaction_3" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="3"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Wow</div></div></div></div></span><span aria-pressed="false" aria-label="Sad" class="_iuw" data-testid="reaction_7" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="7"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Sad</div></div></div></div></span><span aria-pressed="false" aria-label="Angry" class="_iuw" data-testid="reaction_8" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="8"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Angry</div></div></div></div></span></div><div class="_41nt" style="height: 52px;">
</div></div></div></div></div></div></span><span class="_1mto"><span class="_6a _15-7 _3h-u _4k43"><a class="comment_link _5yxe" role="button" href="#" title="Leave a comment" data-ft="{ &quot;tn&quot;: &quot;S&quot;, &quot;type&quot;: 24 }">Comment</a></span></span><span class="_1mto"><span class="_27de _4noj"><a href="/ajax/sharer/?s=2&amp;appid=2305272732&amp;id=1121385471215631&amp;p[0]=1121385471215631&amp;sharer_type=all_modes&amp;av=100011339780683&amp;feedback_referrer=%2Fayush.mandowara&amp;feedback_source=17" rel="dialog" class="share_action_link _5f9b" role="button" tabindex="0" data-ft="{ &quot;tn&quot;: &quot;J&quot;, &quot;type&quot;: 25 }" title="Send this to friends or post it on your Timeline.">Share</a></span></span></div></div>


<a class="comment_link _5yxe" role="button" href="#" title="Leave a comment" data-ft="{ &quot;tn&quot;: &quot;S&quot;, &quot;type&quot;: 24 }">Comment</a>


data-offset-key="fvq43-0-0"
'''


