from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import path_chromedriver

# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

def mac_abhishek():
    import os.path
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")
    return path

# def pc_ayush():
# 	path = 'C:\\testDir\\chromedriver_win32\\chromedriver.exe'
# 	return path

# def pc_akmal():
# 	path = "C:\\Users\\Admin\\Desktop\\chromedriver.exe"
# 	return path

# def desktop_ayush():
# 	path = path_chromedriver.cd_path()
# 	return path

import os

def chromedriver_path():
	abs_dir_path = os.path.abspath(__file__) # absolute file path
	req_path = abs_dir_path.rpartition('\\')
	chrome_driver_path = req_path[0] + '\\chromedriver_win32\\chromedriver.exe'
	return chrome_driver_path

path = chromedriver_path()
