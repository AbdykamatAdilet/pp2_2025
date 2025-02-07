def func(movies):
    sum = 0
    for i in movies:
        sum+=i['imdb']
    return round(sum/len(movies),2)


print(func(movies))