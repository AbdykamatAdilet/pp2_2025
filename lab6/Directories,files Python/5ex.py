def convert(filename, my_list):
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")
    print(f"The list has been written to '{filename}'.")

my_list = ["Apple", "Banana", "Cherry", "Date"]
filename = r"C:\Users\HOME\Desktop\pp2_2025\lab6\Directories,files Python\test.txt"
convert(filename, my_list)
with open(filename, 'r') as file:
    print(file.read())