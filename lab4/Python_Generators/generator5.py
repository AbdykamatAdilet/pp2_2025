def returns(n):
    for i in range(n,-1,-1):
        yield i

res = returns(5)
for i in res:
    print(i)