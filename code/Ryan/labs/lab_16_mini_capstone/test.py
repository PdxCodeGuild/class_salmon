from datetime import *
to_date = date.today()
print(to_date)
print(type(to_date))
seconds1 = datetime.combine(to_date, datetime.min.time(),tzinfo=timezone.utc)
print(seconds1.timestamp(), "line4")
#test = datetime.now.timestamp()

print(date.today(), "7")

test_date = datetime.now(timezone.utc)
print(test_date)
seconds2 = datetime.combine(test_date, datetime.min.time())
print(seconds2.timestamp(), "<<<here")


print(to_date,"line7")
print(type(to_date))
to_date = datetime(2021,6,10)
print(to_date)

# https://finance.yahoo.com/quote/tsla/history
# ?period1=1591747200
# &period2=1623283200
           #1623283200
        #  1623308400

now = datetime.now()
print(now)

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)
print(type(dt_string))

dt = datetime.today()
seconds = dt.timestamp()
print(seconds)*
print(type(seconds))

#to_date_timestamp = time.time(to_date)
from_date = to_date - timedelta(days=365)
print(from_date.date())
print(type(from_date.date()))
seconds3 = datetime.combine(from_date.date(), datetime.min.time(), tzinfo = timezone.utc)
print(int(seconds3.timestamp()))