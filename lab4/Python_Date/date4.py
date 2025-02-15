import datetime

x = datetime.datetime.now()
y = datetime.datetime.now().replace(hour=16)

print((x-y).total_seconds())