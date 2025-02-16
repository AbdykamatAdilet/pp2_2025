def gen(n):
    for i in range(0,n,2):
        yield i

res = gen(18)
for i in res:
    print(i)