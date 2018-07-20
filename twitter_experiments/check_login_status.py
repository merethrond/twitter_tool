from sys_config import path, chrome_options, webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from vault import login_excel
excel_data = pd.read_excel(login_excel)

def login(driver, username, password):
    time.sleep(1)
    driver.get('https://apps.twitter.com/')
    signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
    signIn.click()
    print("Username:", username)
    print("Twitter app opened")

    email = driver.switch_to_active_element()#Maybe we will select element instead of this.
    print(email.text)
    if(email.text == username):
      print('entered correctly')
    else:
      print('incorrectly entered')  
    time.sleep(3)
    email.send_keys(username)
    email.send_keys(Keys.TAB)
    print("email entered")

    time.sleep(1)
    email = driver.switch_to_active_element()
    email.send_keys(password)
    email.send_keys(Keys.RETURN)
    print("password entered")

    time.sleep(2)
    print(driver.current_url)
    if(driver.current_url != 'https://apps.twitter.com/'):
      return False
    return True

def read_login_credentials():
    issues = []
    for username, password in zip(excel_data.username, excel_data.password):
        driver = webdriver.Chrome(executable_path = path)
        
        if (login(driver, username, password)):
            # Will check through app creation later.
            issues.append("active")
            print("Logged in")
        else:
            issues.append("not active")
        driver.close()
    excel_data['issues'] = issues
    excel_data.to_excel(login_excel)

def convert_to_dictionary():
    return {i:j for i, j, k in zip(excel_data.username, excel_data.password, excel_data.issues) if k == 'active'}
