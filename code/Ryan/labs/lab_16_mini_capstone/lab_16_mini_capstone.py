#-----------------------------------------------------------------------------#
# Idea: Make a simple program that takes in historical stock data (OHLC,Volume,date) and displays a line
# graph using Pygal.

# Data csv needs to be provided, user must download CSV from yahoo

#-----------------------------------------------------------------------------#

# 1) Pre-req checks
# Check if local host has the appropriate modules installed
    # if not, prompt user for installation

import datetime
import numpy as np
# pip install numpy
import pandas as pd
# pip install pandas
import pygal
# pip install pygal
from pygal.style import *
import webbrowser
# pip install webbrowser
from datetime import *
import lxml
# pip install lxml

#-----------------------------------------------------------------------------#

# 2) User needs to supply the csv from yahoo

# Inform user with instructions
print(f"""\nA specially formatted CSV file will need to be supplied for the program to continue.
\n\t~~~~~_____Instructions_____~~~~~
1) Enter the ticker of a stock
2) Yahoo finance should automatically open in your browser. If not, please visit: https://finance.yahoo.com/lookup before continuing.
""")

# Lookup URL
# https://finance.yahoo.com/quote/tsla/history?period1=1591747200&period2=1623283200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

# Download URL
#https://query1.finance.yahoo.com/v7/finance/download/OCGN?period1=1591747200&period2=1623283200&interval=1d&events=history&includeAdjustedClose=true

# Get the ticker from user
search_ticker = str(input("Enter a ticker: "))

# Auto set the date period to todays date at midnight, GMT time
to_date = date.today()
seconds_1 = datetime.combine(to_date, datetime.min.time(), tzinfo = timezone.utc)
period_1 = str(int(seconds_1.timestamp()))

# Auto set the date period to 1 year from to_date
from_date = to_date - timedelta(days = 365)
seconds_2 = datetime.combine(from_date, datetime.min.time(), tzinfo = timezone.utc)
period_2 = str(int(seconds_2.timestamp()))

# Convert the csv into a listed dictionary
# Skip the adj price column
search_url= str((f"""https://finance.yahoo.com/quote/{search_ticker}/history/?period1={period_2}&period2={period_1}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"""))
print(search_url)
webbrowser.open(search_url, new = 1)

print(f"""
\n3) Click the 'Download' button in the center of the screen.
4) Save the document in the same folder as this program.
""")

input("Press enter to continue...")

df = pd.read_csv(f"{search_ticker}.csv", usecols=[0,1,2,3,4,6])

# Add column values to lists
dates = []
opens = []
highs = []
mids = []
lows = []
closes = []
means = []
for date in df["Date"]:
    dates.append(date)

for open in df["Open"]:
    opens.append(open)

for high in df["High"]:
    highs.append(high)

for low in df["Low"]:
    lows.append(low)

for close in df["Close"]:
    closes.append(close)

# Daily mids
for each in range(len(highs)):
    #print(each) # <- Index
    daily_mid = (highs[each] - lows[each]) / 2 + lows[each]
    mids.append(daily_mid)

# TODO Mean calcultaion


# Creating the line chart
line_chart = pygal.Line(x_label_rotation = 270, show_minor_x_labels = False, x_labels_major_every = 7, show_dots = True, dots_size = 1, style = DarkStyle)

# Change title to reflect the name of stock
line_chart.title = f"{search_ticker} stock price over 1 year"
line_chart.x_labels = map(str, dates)

# Lines for the KDP_Chart
line_chart.add("Open", opens)
line_chart.add("High", highs, show_dots = False)
line_chart.add("Low", lows, show_dots = False)
line_chart.add("Close", closes)
line_chart.add("Mid", mids)

# Save file in program location
# line_chart.render_to_file(f"{search_ticker}_Chart.svg")

line_chart.render_in_browser()

print(f"""\nThe chart has been created.
Go to the save location from earlier and open {search_ticker}_Chart.svg in your browser to view the results.""")
