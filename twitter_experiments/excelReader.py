import pandas as pd

file_name = "email_credentials.xlsx"

excel_data = pd.read_excel(file_name)  # Opening the file

def convert_to_dictionary():
    return {i:j for i, j, k in zip(excel_data.username, excel_data.password, excel_data.issues) if k == 'done'}

credentials = convert_to_dictionary()
print(credentials)
