def histogram(n_list):
    for num in n_list:
        print(num * '*')

nums = input("Enter the nums separated by space: ")
n_list = [int(elem) for elem in nums.split()]
histogram(n_list)