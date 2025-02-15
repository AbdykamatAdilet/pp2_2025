def gen(squareNum):
    for i in range(squareNum):
        sq = i*i
        yield sq
        
print(list(gen(10)))