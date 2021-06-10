#-----------------------------------------------------------------------------#
# Idea: Make a simple program that takes in historical stock data (OHLC,Volume,date) and displays a line
# graph using Pygal.

# Data csv needs to be provided, user must download CSV from yahoo

#-----------------------------------------------------------------------------#

# 1) Pre-req checks
# Check if local host has the appropriate modules installed
    # if not, prompt user for installation

try:
    import numpy as np
except ImportError:
    print(f"""Numpy is required to continue. Please install numpy in the terminal with the following command:
    pip install numpy""")

try:
    import pandas as pd
except ImportError:
    print(f"""Pandas is required to continue. Please install panda in the terminal with the following command:
    pip install pandas""")

try:
    import pygal
except ImportError:
    print(f"""Pygal is required to contine. Please install pygal in the terminal with the following command:
    pip install pygal""")

try:
    import webbrowser
except ImportError:
    print(f"""webbrowser is required to continue. Please install webbrowser in the terminal with the following command:
    pip install webbrowser""")

#-----------------------------------------------------------------------------#

# 2) User needs to supply the csv from yahoo

# Inform user with instructions
print(f"""A specially formatted CSV file will need to be supplied for the program to continue.
\t_____Instructions_____
\t1) Enter the ticker of a stock
\t2) Yahoo finance should automatically open in your browser. If not, please visit: https://finance.yahoo.com/lookup before continuing.
\t3)
\t3) """)

# Lookup URL
# https://finance.yahoo.com/quote/tsla/history
# ?period1=1591747200
# &period2=1623283200
# &interval=1d
# &filter=history
# &frequency=1d
# &includeAdjustedClose=true
# Download URL
#https://query1.finance.yahoo.com/v7/finance/download/OCGN?period1=1591747200&period2=1623283200&interval=1d&events=history&includeAdjustedClose=true
search_ticker = str(input("Enter a ticker: "))

# Convert the csv into a listed dictionary
# Skip the adj price column
search_url= (f"https://finance.yahoo.com/quote/" + {search_ticker})
webbrowser.open(search_url, new = 1)

df = pd.read_csv("KDP.csv", usecols=[0,1,2,3,4,6])
print(df.head(5))

dates = []
for date in df["Date"]:
    dates.append(date)

opens = []
for open in df["Open"]:
    opens.append(open)

highs = []
for high in df["High"]:
    highs.append(high)

lows = []
for low in df["Low"]:
    lows.append(low)

closes = []
for close in df["Close"]:
    closes.append(close)


# Creating the line chart
line_chart = pygal.Line(x_label_rotation = 270, show_minor_x_labels = False, x_labels_major_every = 7, show_dots = False)

# TODO Change title to reflect the name of stock
line_chart.title = "KDP stock price over 1 year"
line_chart.x_labels = map(str, dates)

# Lines for the KDP_Chart
line_chart.add("Open", opens)
line_chart.add("High", highs)
line_chart.add("Low", lows)
line_chart.add("Close", closes)

# TODO Allow user to specify place to save
line_chart.render_to_file("KDP_Chart.svg")
