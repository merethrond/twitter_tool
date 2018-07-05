from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe')
browser.get('http://www.yahoo.com')

assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

#Get Browser Name
print(browser.name)
 
#Get Title
print(browser.title)
 
#Get Current URL
print(browser.current_url)
 
#Get Current Window Handle
print(browser.current_window_handle)
 
#Get All Window Handles
handles_list=browser.window_handles
 
#Get Page Source
#print(browser.page_source)
#browser.quit()
'''
browser.maximize_window()
browser.minimize_window()


browser.back()
browser.forward()
browser.refresh()


Find Element(s) By ID
element = browser.find_element_by_id("txt_1")
elements = browser.find_elements_by_id("txt_1")
 
#Find Element By XPATH
browser.find_element_by_xpath("//input")
 
#Find Element By Link Text
browser.find_element_by_link_text("Products")
 
#Find Element By Link Text
browser.find_element_by_link_text("Products")
 
#Find Element By Partial Link Text
browser.find_element_by_partial_link_text('Sign')
 
#Find Element By Name
browser.find_elements_by_name('foo')
 
#Find Element By Tag Name
browser.find_elements_by_tag_name('Input')
 
#Find Element By Class Name
browser.find_elements_by_class_name('breadcrumb')
 
#Find Element By CSS Selector
browser.find_elements_by_css_selector('input[name="txt"]')
#Get all cookies in a list
cookies_list = browser.get_cookies
 
#Get a Cookie value
cookie_value = browser.get_cookie("my_cookie")
 
#Delete a Cookie
browser.delete_cookie("my_cookie")
 
#Delete all Cookies
browser.delete_all_cookies()
 
#Add Cookie
browser.add_cookie({"name:value"})








browser.switch_to.active_element
 
browser.switch_to.alert
 
browser.switch_to.default_content()
 
# You can pass Window Name or Handle to switch between windows
browser.switch_to.window("window_name")
 
#You can switch to frame using Name, ID, Index & WebElement
browser.switch_to.frame(1)
 
browser.switch_to.parent_frame()


'''