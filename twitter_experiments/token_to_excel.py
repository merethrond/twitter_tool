import pandas as pd
# dataFrame = pd.read_excel('filename.xlsx', sheet_name = "Sheet1")
# print(dataFrame)

# df = pd.DataFrame()

# row = pd.Series([1,2,3],["A","B","C"])

# print(row)

df = pd.read_excel('filename.xlsx', sheet_name = "Sheet1")
b = '06FHqJnnsPrbLsVbIB8wMJZCN5BQYJZlJjF8Y00aj3BnT'
c = '1012220506164957184-cY7KoZK6nerQdpBBPm1opRXA3Ve11K'
d = 'R9mga7BKF0LqjoS0rXIcPYhscmIHUJwm9hJxIYCj8wOVqtDpue'
e = 'hW11F02VpY4ryBxc0AioEUl9g'

# consumer_key:
# consumer_secret:
# No access button found
# access_token:
# access_token_secret:
# b = '1'
# c = '2'
# d = '3'
# e = '4'

a = [[b,c,d,e]]

# list = [[]]
df = df.append(pd.DataFrame(a, columns=['Access Secret','Access Token','Consumer Secret','Consumer Token']),ignore_index=True)

df.to_excel('filename.xlsx')
print(df)
# import openpyxl



# import xlsxwriter

# workbook   = xlsxwriter.Workbook()

# worksheet1 = workbook.add_worksheet()
# print(worksheet1)
# # worksheet1 = workbook.add_worksheet()
# # worksheet2 = workbook.add_worksheet()
# worksheet = workbook.worksheets()
# print(worksheet)
# for i in workbook.worksheets():
# 	print(i)
# # worksheet.write_row()

# workbook.close()













# from xlutils.copy import copy    
# from xlrd import open_workbook

# book_ro = open_workbook(r"C:\testDir\Bots\twitter_experiments\token_credentials.xlsx")
# book = copy(book_ro)  # creates a writeable copy
# sheet1 = book.get_sheet(0)  # get a first sheet

# colx = 1
# for rowx in range(1):
#     # Write the data to rox, column
#     sheet1.write(rowx,colx, url)
#     sheet1.write(rowx,colx+1, count)

# book.save(r"C:\testDir\Bots\twitter_experiments\token2_credentials.xlsx")
