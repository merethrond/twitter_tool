# import inspect
# print (inspect.stack()[0][1])

import os
# dir_path = os.path.dirname(__file__) # relative directory path
abs_dir_path = os.path.abspath(__file__) # absolute file path
# file_name = os.path.basename(__file__) # the file name only
# print(dir_path,"< DIR ",abs_dir_path, " < ABS",file_name,'< file_name')

req_path = abs_dir_path.rpartition('\\')

# print('REQ:',req_path[0])

chrome_driver_path = req_path[0] + '\\chromedriver_win32\\chromedriver.exe'
# print("CD path:",chrome_driver_path)
def cd_path():
	return chrome_driver_path