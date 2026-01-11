import datetime as dt

#Current date and time
now = dt.datetime.now()

#Get certain year, month, day ect
year = now.year
month = now.month
day_of_week = now.weekday()

#Set specific date
date_of_birth = dt.datetime(year=1998, month=10, day=16, hour=1)
print(date_of_birth)