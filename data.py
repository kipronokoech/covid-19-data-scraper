from scraper import aims, world
from pandas import ExcelWriter
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
my_url = "https://www.worldometers.info/coronavirus/"

world = world(my_url)
print(list(world.dtypes))
aims = aims(my_url)
scope = (["https://spreadsheets.google.com/feeds",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive"])
creds =  ServiceAccountCredentials.from_json_keyfile_name("./assets/api.json",scope)
client = gspread.authorize(creds)
sheets = client.open("COVID-19").worksheets()
print(sheets)
sheet = client.open("COVID-19").worksheet("TS_TOTAL")
total = sheet.get_all_records()
total = pd.DataFrame(total)
sheet1 = client.open("COVID-19").worksheet("TS_ACTIVE")
active = sheet1.get_all_records()
active = pd.DataFrame(active)
with ExcelWriter('data.xlsx') as writer:
    world.to_excel(writer,sheet_name="World")
    aims.to_excel(writer,sheet_name="AIMS")
    total.to_excel(writer, sheet_name='Total')
    active.to_excel(writer, sheet_name='Active')