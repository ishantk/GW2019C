import datetime
# import datetime as dt

today = datetime.datetime.today()
print(today)

tomorrow = datetime.datetime(2019, 5, 20, 12, 12, 12, 1234)
print(tomorrow)

howMany = tomorrow - today
print(howMany)