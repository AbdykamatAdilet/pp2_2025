import datetime

x = datetime.datetime.now()

def drop(x):
    ds = x.replace(microsecond=0)
    return ds

print(drop(x))