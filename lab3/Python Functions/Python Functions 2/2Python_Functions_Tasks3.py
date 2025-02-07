def score_5_5(genre):
    result = []
    for m in movies:
        if m['category'] == genre:
                result.append(m['name'])
    return result

nameofcategory = input("Enter the name of the category:")
print(score_5_5(nameofcategory))