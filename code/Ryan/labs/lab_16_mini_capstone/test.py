import requests
response = requests.get("https://finance.yahoo.com/quote/tsla/history?period1=1591747200&period2=1623283200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true")
#data = response.json()
print(response)
#print(data)
