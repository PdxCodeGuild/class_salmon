

from datetime import datetime



# from datetime import datetime
# d = datetime.now()
# print(type(d)) # <class 'datetime.datetime'>
# print(d) # 2021-04-20 11:25:01.027856
# print(d.year) # 2021
# print(d.month) # 4
# print(d.day) # 20
# print(d.hour) # 11
# print(d.minute) # 26
# print(d.second) # 27


# instantiation
# d = datetime(2020, 5, 17)
# print(d.month)

# x = int('5') # 5
# x = str(5) # '5'

# d = datetime.strptime('20-APR-2021', '%d-%b-%Y')
# print(d) # 2021-04-20 00:00:00


# Create Date ==================================================================
# Write a function that creates and returns a new datetime given the components

def create_date(month, day, year):
    return datetime(year, month, day)
print(create_date(4, 20, 2021)) # 2021-04-20 00:00:00


# Get Year =====================================================================
# Write a function that returns the year of a given datetime

def get_year(dt):
    return dt.year
print(get_year(datetime(2021, 4, 20))) # 2021


# Parse Date ===================================================================
# Write a function that converts the given string into a datetime

def parse_date(date_string):
    return datetime.strptime(date_string, '%B %d, %Y')
print(parse_date('April 20, 2021')) # 2021-04-20 00:00:00


# Parse Datetime ===============================================================
# Write a function that converts a given string into a datetime
def parse_datetime(date_string):
    return datetime.strptime(date_string, '%B %d, %Y %I:%M %p')
print(parse_datetime('April 20, 2021 09:30 AM')) # 2021-04-20 09:30:00

# Format Datetime ==============================================================
# Write a function that converts the given datetime into a string
def format_datetime(dt):
    return dt.strftime('%B %d, %Y %I:%M %p') # April 20, 2021 09:30 AM
print(format_datetime(datetime(2021, 4, 20, 9, 30)))

