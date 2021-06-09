#-----------------------------------------------------------------------------#
# Idea: Make a simple program that takes in a stock ticker and displays a line
# graph using Pygal.

# Welcome to Alpha Vantage! Here is your API key: NBKE32QFCBV6LH9Z.
# Please record this API key at a safe place for future data access.

#-----------------------------------------------------------------------------#
# iexfinance module needs to be installed

    # Install command
    # pip install iexfinance

    # For more information visit: https://addisonlynch.github.io/iexfinance/stable/install.html

# numpy module needs to be installed

    # Install command
    # pip install numpy

# Requests module needs to be installed

    # Install command
    # python -m pip install requests

    # For more information visit: https://pypi.org/project/requests/

#  Pygal needs to be installed.

    # Install command for Mac or Linux
    # pip install --user pygal

    # Install command for Windows
    # python -m pip install --user pygal

    # For more information visit: http://www.pygal.org/en/stable/#

# API Reference and data provided by iexcloud.io
# Refer to https://iexcloud.io/docs/api/
#-----------------------------------------------------------------------------#
# Overview
# 1. User inputs
    # a. ticker
    # b. time
        # b1. TODO allow custom date range

# 2. An http request will be sent to

#import requests
import numpy as np
import pandas as pd
import pygal

# # Building the request string
# base = "https://sandbox.iexapis.com/"
# version = "stable/"
# symbol = "IBM"
# endpoint_path = "stock/" + f"{symbol}" + "/quote"
# token = "Tpk_bd3952246da84d349922e84b332db2f4"
# query_string_parameters = f"token={token}"
# print(endpoint_path)
# api_request = f"{base}" + f"{version}" + f"{endpoint_path}" + "?" + f"{query_string_parameters}"
# print(api_request)
#
# # Initiating the request
# response = requests.get(api_request)
# print(response) # <Response [200]>
# response_json = response.json()
# print(response_json)

# Convert the csv into a listed dictionary
# Skip the adj price column

df = pd.read_csv("KDP.csv", usecols=[0,1,2,3,4,6])
print(df.head(5))

dates = []
for date in df["Date"]:
    dates.append(date)

opens = []
for open in df["Open"]:
    opens.append(open)

print(opens)
# Creating the line chart
line_chart = pygal.Line()
# TODO Change title to reflect the name of stock
line_chart.title = "KDP stock price over 1 year"
line_chart.x_labels = map(str, dates)

# Lines for the KDP_Chart
line_chart.add("Open", opens)

# TODO Allow user to specify place to save
line_chart.render_to_file("KDP_Chart.svg")
