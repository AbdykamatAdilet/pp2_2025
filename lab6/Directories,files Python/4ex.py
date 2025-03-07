def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
    return line_count

filename = r"C:\Users\HOME\Desktop\pp2_2025\lab6\Directories,files Python\test.txt"
num_lines = count_lines(filename)
print(f"The file '{filename}' contains {num_lines} lines.")