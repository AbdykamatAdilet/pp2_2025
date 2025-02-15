def gen(n):
    for i in range(0,n,2):
        yield i

print(list(gen(18)))