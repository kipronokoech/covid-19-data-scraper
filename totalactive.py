import os
from scraper import aims, world
from pandas import ExcelWriter
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime
os.chdir("/home/kiprono/Documents/PS_AND_RESEARCH/Projects/Incomplete/covid-19/")
try:
    scope = (["https://spreadsheets.google.com/feeds",
              "https://www.googleapis.com/auth/spreadsheets",
              "https://www.googleapis.com/auth/drive.file",
              "https://www.googleapis.com/auth/drive"])
    creds =  ServiceAccountCredentials.from_json_keyfile_name("./assets/api.json",scope)
    client = gspread.authorize(creds)

    sheet = client.open("COVID-19").worksheet("test_total")

    my_url = "https://www.worldometers.info/coronavirus/"

    aims1 = aims(my_url)
    #AIMS sheet
    aims11 = aims1.reset_index(drop=False)
    aim_sheet = client.open("COVID-19").worksheet("test_aims")
    aims11 = aims11.replace(np.nan, '', regex=True)
    aim_sheet.update([aims11.columns.values.tolist()] + aims11.values.tolist())
    aim_sheet.update_cell(2, 13, str(datetime.today()))
    # TOTAL CASES DEPLOYMENT
    a = int(aims1.loc[["South Africa"]]["TotalCases"])
    b = int(aims1.loc[["Cameroon"]]["TotalCases"])
    c = int(aims1.loc[["Senegal"]]["TotalCases"])
    d = int(aims1.loc[["Ghana"]]["TotalCases"])
    e = int(aims1.loc[["Rwanda"]]["TotalCases"])
    f = datetime.today().strftime('%d/%m/%Y')
    ff = str(datetime.today())
    row = [f,a,b,c,d,e,ff]
    data = sheet.get_all_records()

    #sheet.append_row(row,1)

    last = sheet.row_values(len(data)+1)
    if last[0]==f:
        data = sheet.get_all_records()
        sheet.delete_row(len(data) + 1)
        data2 = sheet.get_all_records()
        sheet.insert_row(row, len(data2) + 2)

    else:
        data2 = sheet.get_all_records()
        sheet.insert_row(row, len(data2) + 2)


    # ACTIVE CASES DEPLOYMENT
    sheet2 = client.open("COVID-19").worksheet("test_active")

    aa = int(aims1.loc[["South Africa"]]["ActiveCases"])
    ab = int(aims1.loc[["Cameroon"]]["ActiveCases"])
    ac = int(aims1.loc[["Senegal"]]["ActiveCases"])
    ad = int(aims1.loc[["Ghana"]]["ActiveCases"])
    ae = int(aims1.loc[["Rwanda"]]["ActiveCases"])
    af = datetime.today().strftime('%d/%m/%Y')
    aff = str(datetime.today())
    row2 = [af,aa,ab,ac,ad,ae,aff]

    #sheet.append_row(row,1)
    data2 = sheet2.get_all_records()
    last2 = sheet2.row_values(len(data2)+1)
    if last2[0]==af:
        data2 = sheet2.get_all_records()
        sheet2.delete_row(len(data2)+1)
        data2 = sheet2.get_all_records()
        sheet2.insert_row(row2,len(data2)+2)
    else:
        data2 = sheet2.get_all_records()
        sheet2.insert_row(row2, len(data2) + 2)
    with open("/home/kiprono/Desktop/time.txt","a+") as f:
        f.write(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')+"\n")
except:
    with open("/home/kiprono/Desktop/error.txt","w+") as f:
        f.write("There is a mistake.")
