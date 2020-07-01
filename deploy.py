# in this script we will deploy the output of the other
# py files into excel file
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = (["https://spreadsheets.google.com/feeds",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive"])
creds =  ServiceAccountCredentials.from_json_keyfile_name("./assets/api.json",scope)
client = gspread.authorize(creds)
sheet = client.open("data").worksheet("World")
#get all the record on the sheet
data = sheet.get_all_records()
#getting the row
row = sheet.row_values(3)
print(row)
#getting the column
col = sheet.col_values(1)
print(col)
#get values on a specific cell
cell = sheet.cell(1,2).value
print(cell)
#insert row
#sheet.resize(len(data))
insert_row = ["Yae",47600]
#sheet.insert_row(insert_row,1)
#sheet.delete_row(1)
#sheet.insert_row(insert_row,1)
data2 = sheet.get_all_records()
print(len(data2))
sheet.insert_row(["after the last"],len(data2)+2)
sheet.delete_row(len(data2)+1)
data2 = sheet.get_all_records()
sheet.insert_row(["last"],len(data2)+1)

