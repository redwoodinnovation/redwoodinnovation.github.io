# Libraries
import pandas as pd
import gspread as gs
from datetime import date
from datetime import timedelta
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

# Authorization
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
gc = gs.authorize(credentials)

# Get today's date & calculate yesterday's date
today = date.today()
yesterday = today - timedelta(days = 1)

# Convert date to string for concatenation
day = str(yesterday)

# Specify CSV parameters
node = '103'
timestop = '16:30:00'
timestart = '15:30:00'
parameter = 'co2_dry_sync'

# Read data into dataframe from remote CSV
df = pd.io.parsers.read_csv("http://128.32.208.8/node/"+node+"/measurements_all/csv?name=Supersite&interval=60&variables="+parameter+"&start="+day+"%20"+timestart+"&end="+day+"%20"+timestop+"", on_bad_lines="skip", index_col=False, parse_dates=False)

# Spreadsheet & sheet ID
spreadsheet_key = '1i7I8GU8UnDoeGHtY4Pu45vd546xVyDjxp0Mxk5vXqFk'

# sheetName = 'Sheet1'			# Not necessary when gsheet has only one sheet.  

# Update spreadsheet with dataframe data. Add sheetName if gsheet has multiple sheets 
d2g.upload(df, spreadsheet_key, credentials=credentials, row_names=False)

# d2g.upload(df, spreadsheet_key, sheetName, credentials=credentials, row_names=True)