def gen(squareNum):
    for i in range(squareNum):
        sq = i*i
        yield sq
        
res = gen(10)
for i in res:
    print(i)