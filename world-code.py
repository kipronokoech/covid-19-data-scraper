import os
from scraper import world
import numpy as np
from pandas import ExcelWriter
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime
os.chdir("/home/kiprono/Documents/PS_AND_RESEARCH/Projects/Incomplete/covid-19/")

scope = (["https://spreadsheets.google.com/feeds",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive"])

creds =  ServiceAccountCredentials.from_json_keyfile_name("./assets/api.json",scope)

client = gspread.authorize(creds)

sheet = client.open("COVID-19")
#sheet.add_worksheet(title="test_world", rows="100", cols="20")

worksheet = sheet.worksheet("test_world")
#same sheet = client.open("COVID-19").worksheet("World")
my_url = "https://www.worldometers.info/coronavirus/"


world1 = (world(my_url)).reset_index(drop=False)


world1 = world1.replace(np.nan, '', regex=True)


worksheet.update([world1.columns.values.tolist()] + world1.values.tolist())
worksheet.update_cell(2,13,str(datetime.today()))
