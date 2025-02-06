def unique(num_list):
    arr = []
    for i in num_list:
        if i not in arr:
            arr.append(i)
    return arr

nums = input("Enter the nums:")
num_list = nums.split()
res = unique(num_list)
print(res)