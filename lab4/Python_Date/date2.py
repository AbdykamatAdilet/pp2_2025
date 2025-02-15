import datetime

Today = datetime.datetime.now()
Yesterday = Today - datetime.timedelta(1)
Tomorrow = Today + datetime.timedelta(1)

print('Today:' + str(Today))
print('Yesterday:' + str(Yesterday))
print('Tomorrow:' + str(Tomorrow))