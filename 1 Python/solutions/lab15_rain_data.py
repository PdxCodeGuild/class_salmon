


# from datetime import datetime

# day1_date = datetime(2021, 4, 19)
# day1_total = 5
# day2_date = datetime(2021, 4, 20)
# day2_total = 8
# day3_date = datetime(2021, 4, 21)
# day3_total = 1

# # print(day1_date)
# # print([day1_date])

# data = [(day1_date, day1_total), (day2_date, day2_total), (day3_date, day3_total)]
# print(data[0][1]) # 5

# data = [{
#     'date': day1_date,
#     'daily_total': day1_total
# },{
#     'date': day2_date,
#     'daily_total': day2_total
# },{
#     'date': day3_date,
#     'daily_total': day3_total
# }]
# print(data[0]['daily_total'])


# import matplotlib.pyplot as plt
# from datetime import datetime
# x_values = [datetime(2018, 5, 23), datetime(2018, 5, 24)]
# y_values = [0.56, 1.23]
# plt.plot(x_values, y_values)
# plt.show()



import re
import requests
from datetime import datetime
import matplotlib.pyplot as plt


def get_data():
    url = 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain'
    response = requests.get(url)
    data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', response.text)
    # [('27-AUG-1998', '0'), ('26-AUG-1998', '0')]
    for i in range(len(data)):
        date = datetime.strptime(data[i][0], '%d-%b-%Y')
        daily_total = int(data[i][1])*0.01*2.54 # in cm
        # data[i] = (date, daily_total)
        data[i] = {'date': date, 'daily_total': daily_total}
    return data

def chart_average_rain_per_year(data):

    # years = list(range(data[-1]['date'].year, data[0]['date'].year+1))
    # years = list(range(1998, 2022))

    years = []
    for row in data:
        year = row['date'].year
        if year not in years:
            years.append(year)
    years.sort()
    
    year_averages = []
    for year in years:
        year_average = 0
        year_count = 0
        for row in data:
            if row['date'].year == year:
                year_average += row['daily_total']
                year_count += 1
        year_average /= year_count
        year_averages.append(year_average)
    
    plt.bar(years, year_averages)
    plt.show()

data = get_data()
chart_average_rain_per_year(data)





