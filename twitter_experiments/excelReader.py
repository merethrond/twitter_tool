import pandas as pd
from key_file_vault import email_excel


excel_data = pd.read_excel(email_excel)  # Opening the file

def convert_to_dictionary():
    return {i:j for i, j, k in zip(excel_data.username, excel_data.password, excel_data.issues) if k == 'active'}

credentials = convert_to_dictionary()
#Excluding this email because of phone verification requirement upon app creation.

print(credentials)
