a = int(input('Write first num:'))
b = int(input('Write second num:'))

def squares(a,b):
    for i in range(a,b+1):
        yield i*i

res = squares(a,b)
for i in res:
    print(i)