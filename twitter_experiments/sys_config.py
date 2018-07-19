import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")
mac_config = DRIVER_BIN

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)


pc_config
