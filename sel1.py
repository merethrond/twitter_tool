from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe')
browser.get('http://www.yahoo.com')

assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

#browser.quit()